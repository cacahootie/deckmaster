from flask import Flask, render_template

from . import app
from process_site import process_site


def index():
    return render_template('html/base.html', **process_site())