"""Process `site.json` and bower package tools."""

import os
import json
import subprocess
from functools import partial

from flask import Flask, render_template, g, redirect, current_app

from gitloader import git_show

try:
    from app import app
except ImportError:
    from deckmaster.app import app

component_dir = 'static/components'
bower_str = 'bower install --config.directory="%s" %s > /dev/null'

def get_pkg_dir(package):
    """Join the component and package directory."""
    return os.path.join(component_dir, package)

def get_pkg_main(package):
    """Check `package.json` then `bower.json` for the main included file."""
    pkg = json.load(
        open(os.path.join(get_pkg_dir(package), 'bower.json'))
    )
    if isinstance(pkg['main'],list):
        return [os.path.join(get_pkg_dir(package), p) for p in pkg['main']]
    else:
        return os.path.join(get_pkg_dir(package), pkg['main'])

def check_pkg(package):
    """CHeck if the package exists, if not use bower to install."""
    if not os.path.exists(os.path.join(component_dir, package)):
        subprocess.call(
            bower_str % (component_dir, package),
            shell = True
        )
    return True

def script_or_style(path):
    if path.endswith('js'):
        return 'script'
    elif path.endswith('css'):
        return 'style'
    else:
        print "Script or style? " + path

def process_bower(deps):
    retval = {'styles':[], 'scripts':[]}
    try:
        for pkg in deps['bower']:
            check_pkg(pkg)
            main =  get_pkg_main(pkg)
            if isinstance(main,list):
                pkgassets = {}
                for path in reversed(main):
                    try:
                        pkgassets[script_or_style(path)+'s'] = [path]
                    except TypeError:
                        pass
                retval['scripts'] += pkgassets['scripts']
                retval['styles'] += pkgassets['styles']
            else:
                retval[script_or_style(main)+'s'].append(main)
    except KeyError:
        pass
    return retval

def process_local(deps):
    retval = {'styles':[], 'scripts':[]}
    try:
        for path in deps['local']:
            retval[script_or_style(path)+'s'].append(path)
    except KeyError:
        pass
    return retval


def process_deps(deps):
    """Process script element in the config for local vs bower components."""
    local, bower = process_local(deps), process_bower(deps)
    retval = {}
    for tag in local:
        retval[tag] = local[tag] + bower[tag]
    return retval


def process_route(route):
    def route_handler(revid = None, path = None):
        g.revid = revid
        try:
            return render_template(
                'html/base.html', **process_deps(route['deps'])
            )
        except AttributeError:
            return 'Not Found', 404
    return route_handler


def lazy_router(revid, path = None):
    g.revid = revid
    if path is None:
        path = ''
    if not path.startswith('/'):
        path = '/' + path
    cfgstr = git_show('./site.json', revid)
    return process_route(json.loads(cfgstr)[path])(revid, path)


def process_site(site = None, revid = None):
    """Process `site.json` based on the config and CLI options."""
    if site is None:
        try:
            site = json.load(open('site.json'))
        except IOError:
            return []
    if 'deps' in site:
        return [
            ('/', 'index', process_route(site)),
            ('/<revid>/', 'index_revid', process_route(site)),
        ]
    retval = [
        ('/<revid>/', 'revid_lazy_index', lazy_router),
        ('/<revid>/<path:path>', 'revid_lazy', lazy_router),
    ]
    for rt in site:
        retval.append((rt, 'index' if rt=='/' else rt, process_route(site[rt])))
    return retval
