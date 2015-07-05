"""Process `site.json` and bower package tools."""

import os
import json
import subprocess

try:
    from app import app
except ImportError:
    from deckmaster.app import app

component_dir = 'static/components'
bower_str = 'bower install --config.directory="%s" %s'

def get_pkg_dir(package):
    """Join the component and package directory."""
    return os.path.join(component_dir, package)

def get_pkg_main(package):
    """Check `package.json` then `bower.json` for the main included file."""
    try:
        pkg = json.load(
            open(os.path.join(get_pkg_dir(package), 'package.json'))
        )
    except IOError:
        pkg = json.load(
            open(os.path.join(get_pkg_dir(package), '.bower.json'))
        )
    return os.path.join(get_pkg_dir(package), pkg['main'])

def check_pkg(package):
    """CHeck if the package exists, if not use bower to install."""
    if not os.path.exists(os.path.join(component_dir, package)):
        subprocess.call(
            bower_str % (component_dir, package),
            shell = True
        )
    return get_pkg_main(package)

def process_script(script):
    """Process script element in the config for local vs bower components."""
    if 'bower' in script:
        return check_pkg(script['bower'])
    return script

def process_site():
    """Process `site.json` based on the config and CLI options."""
    if app.config.get('WORKDIR'):
        site = json.load(open(os.path.join(app.config['WORKDIR'], 'site.json')))
    else:
        site = json.load(open('site.json'))
    try:
        site['scripts'] = [process_script(x) for x in site['scripts']]
    except KeyError:
        pass
    return site
