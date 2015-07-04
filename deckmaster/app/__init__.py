"""deckmaster app"""

import os
import json

from flask import Flask

app = Flask(
    __name__,
    static_folder = os.path.join(os.getcwd(),'static'),
    static_url_path='/static',
    template_folder=os.path.join(
        os.path.abspath(os.path.dirname(__file__)),'templates')
)

import index