"""deckmaster app"""

import os
import json
from urllib import unquote

from flask import Flask, request

from gitloader import GitLoader, git_static

app = None

class FlaskGit(Flask):

	def send_static_file(self,filename):
		query_string = unquote(request.query_string)
		try:
			if query_string.startswith('@'):
				return git_static(filename, query_string)
		except AttributeError:
			pass
		return Flask.send_static_file(self,filename)


def get_instance():
	app = FlaskGit(
	    __name__,
	    static_folder = os.path.join(os.getcwd(),'static'),
	    static_url_path='/static',
	    template_folder=os.path.join(
	        os.path.abspath(os.path.dirname(__file__)),'templates')
	)
	
	from process_site import process_site

	for route in process_site():
		app.add_url_rule(*route)

	app.config['basedir'] = os.path.realpath(
		os.path.join(os.path.dirname(__file__),'..','..')
	)

	print app.config['basedir']

	return app