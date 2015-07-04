from flask import Flask, render_template

from app import app
from process_site import process_site


@app.route("/")
def index():
    return render_template('html/base.html', **process_site())