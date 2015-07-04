"""deckmaster app"""

import os
import json

from flask import Flask, render_template

from process_site import process_site


app = Flask(
    __name__,
    static_folder = os.path.join(os.getcwd(),'static'),
    static_url_path='/static',
    template_folder=os.path.join(os.path.dirname(__file__),'templates')
)


@app.route("/")
def index():
    return render_template('html/base.html', **process_site())
