"""deckmaster app"""

import os
import json

from flask import Flask, render_template
app = Flask(
    __name__,
    static_folder = os.path.join(os.getcwd(),'static'),
    static_url_path='/static'
)

@app.route("/")
def index():
    return render_template('html/base.html', **json.load(open('site.json')))
