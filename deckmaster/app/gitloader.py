"""Jinja2-Git Template Loader"""

from subprocess import check_output
import os
import json

import jinja2

from flask import request, current_app


def git_show(base,revid):
    """Git show the base/revid."""
    return check_output(['git show %s:%s ' % (revid, base)], shell=True)


class GitLoader(jinja2.BaseLoader):
    """Load a template from a specific git revision."""
    def get_source(self, environment, template):
        if '@' in request.url:
            src = git_show(template, request.path.rsplit('@',1)[1])
            return src, template, lambda: True
        templpath = os.path.join(current_app.template_folder, template)
        return open(templpath).read(), template, lambda: False


def git_static(path, revid):
    fullpath = request.path
    if fullpath[0] == '/':
        fullpath = fullpath[1:]
    fullpath = os.path.join(os.getcwd(), fullpath)
    if fullpath.startswith(current_app.config['basedir']):
        fullpath = fullpath[ len(current_app.config['basedir']) + 1 : ]
    return git_show(fullpath, revid[1:])
