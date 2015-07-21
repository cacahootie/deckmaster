"""Jinja2-Git Template Loader"""

from subprocess import check_output
import os
import json
from mimetypes import guess_type

import jinja2

from flask import request, current_app, g


def git_show(base,revid):
    """Git show the base/revid."""
    if revid.startswith('@'):
        revid = revid[1:]
    return check_output(['git show %s:%s ' % (revid, base)], shell=True)


class GitLoader(jinja2.BaseLoader):
    """Load a template from a specific git revision."""
    def get_source(self, environment, template):
        if '@' in request.path:
            src = git_show(template, request.path.rsplit('@',1)[1])
            return src, template, lambda: True
        if g.get('revid') is not None:
            templpath = os.path.join(current_app.template_folder, template)
            if templpath.startswith(current_app.config['basedir']):
                templpath = templpath[ len(current_app.config['basedir']) + 1 :]
            src = git_show(templpath, g.revid)
            return src, template, lambda: True
        templpath = os.path.join(current_app.template_folder, template)
        return open(templpath).read(), template, lambda: False


def git_static(path, revid):
    if path[0] == '/':
        path = path[1:]
    path = os.path.join(os.getcwd(), path)
    if path.startswith(current_app.config['basedir']):
        path = path[ len(current_app.config['basedir']) + 1 : ]
    return git_show(path, revid), 200, {'Content-Type': guess_type(path)}

def git_static_nested(path, revid):
    if path.startswith('components'):
        return current_app.send_static_file(path)
    return git_static(os.path.join('static', path), revid)
