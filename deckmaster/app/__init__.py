"""deckmaster app"""

import os
import json

from flask import Flask


app = None

def get_instance():
	app = Flask(
	    __name__,
	    static_folder = os.path.join(os.getcwd(),'static'),
	    static_url_path='/static',
	    template_folder=os.path.join(
	        os.path.abspath(os.path.dirname(__file__)),'templates')
	)
	
	from process_site import process_site

	for route in process_site():
		app.add_url_rule(*route)

	return app