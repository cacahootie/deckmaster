"""deckmaster app"""

import os
import json
from urllib import unquote

from flask import Flask, request

from gitloader import GitLoader, git_static, git_static_nested

app = None

class FlaskGit(Flask):

	def __init__(self, *args, **kwargs):		
		Flask.__init__(self, *args, **kwargs)
		self.jinja_loader = GitLoader()

	def send_static_file(self, filename, revid = None):
		query_string = unquote(request.query_string)
		try:
			if query_string.startswith('@'):
				return git_static(request.path, query_string)
			elif revid is not None:
				return git_static(filepath, revid)
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

	app.template_folder = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'templates'
    )
	
	from process_site import process_site

	for route in process_site():
		app.add_url_rule(*route)

	app.add_url_rule(
		'/<revid>/static/<path:path>', 'static_revid', git_static_nested
	)

	app.config['basedir'] = os.path.realpath(
		os.path.join(os.path.dirname(__file__),'..','..')
	)

	print app.config['basedir']

	return app
