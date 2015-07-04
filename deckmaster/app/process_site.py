"""Process `site.json` """

import os
import json
import subprocess

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
    if not os.path.exists(os.path.join(component_dir, package)):
        subprocess.call(
            bower_str % (component_dir, package),
            shell = True
        )
    return get_pkg_main(package)

def process_script(script):
    if 'bower' in script:
        return check_pkg(script['bower'])
    return script

def process_site():
    site = json.load(open('site.json'))
    try:
        site['scripts'] = [process_script(x) for x in site['scripts']]
    except KeyError:
        pass
    return site
