"""Process `site.json` """

import os
import json
import subprocess

component_dir = 'static/components'
bower_str = 'bower install --config.directory="%s" %s'

def get_pkg_dir(package):
    return os.path.join(component_dir, package)

def get_pkg_main(package):
    try:
        pkg = json.load(
            open(os.path.join(get_pkg_dir(package), 'package.json'))
        )
    except IOError:
        pkg = json.load(
            open(os.path.join(get_pkg_dir(package), '.bower.json'))
        )
    return os.path.join(get_pkg_dir(package), pkg['main'])

def process_script(script):
    if 'bower' in script:
        if not os.path.exists(os.path.join(component_dir, script['bower'])):
            subprocess.call(
                bower_str % (component_dir, script['bower']),
                shell = True
            )
        script = get_pkg_main(script['bower'])
    return script

def process_site():
    site = json.load(open('site.json'))
    try:
        site['scripts'] = [process_script(x) for x in site['scripts']]
    except KeyError:
        pass
    print site
    return site