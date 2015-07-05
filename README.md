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

Here's some more detail on the CLI options for deckmaster:

	$ deckmaster --help
	usage: deckmaster [-h] [--no-debug] [--workdir [WORKDIR]]

	Serve bower packages and local assets.

	optional arguments:
	  -h, --help            show this help message and exit
	  --no-debug, -N        don't show debugger on exception or reload on file
	                        update
	  --workdir [WORKDIR], -w [WORKDIR]
	                        specify a working directory other than current
	                        directory

`site.json`
=============

Provides the structure of the assets served by deckmaster.

Simple example, serves only an index route of styles and scripts:

```javascript	
{
    "styles": [
        "static/style.css"
    ],
    "scripts": [
        "static/script.js",
        {"bower":"d3"},
        {"bower":"leaflet"}
    ]
}
```
