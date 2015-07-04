# deckmaster

Provide compiled HTML, static assets and templated cards from `site.json`, with
a development server and deployment compiler (planned).

Installation
==============

	pip install deckmaster

Usage
=======

Switch to a directory containing a `site.json`, and execute

	deckmaster

This will run deckmaster in dev mode, and will serve the site as defined in
`site.json`.

Development
=============

A vagrant box is included in this setup, mostly to test the installation of
the package itself without sullying one's own path.
