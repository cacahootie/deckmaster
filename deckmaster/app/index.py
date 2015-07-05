"""Default index route for deckmaster, serving a simple `site.json`."""

from flask import Flask, render_template

from . import app
from process_site import process_site


def index():
    """Render an `index.html` using the `site.json` configuration."""
    return render_template('html/base.html', **process_site())