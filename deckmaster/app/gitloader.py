"""Jinja2-Git Template Loader"""

from subprocess import check_output
import os

import jinja2

from flask import request


class GitLoader(jinja2.BaseLoader):
    """Load a template from a specific git revision."""
    def get_source(self, environment, template):
        return open(template).read(), template, lambda: True
