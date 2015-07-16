"""Jinja2-Git Template Loader"""

from subprocess import check_output
import os

import jinja2

from flask import request


class GitLoader(jinja2.BaseLoader):
    """Load a template from a specific git revision."""
    def get_source(self, environment, template):
        if '@' in request.url:
            base, revid = request.path.rsplit('@',1)
            print 'git show %s:%s ' % (revid, template)
            src = check_output(
                ['git show %s:%s ' % (revid, template)],
                shell=True
            )
            return src, base, lambda: True
        return open(template).read(), template, lambda: False
