# deckmaster

Provide compiled HTML, static assets and templated cards from `site.json`, with
a development server and deployment compiler (planned).

Prerequisites
==============

I'll leave you to install node/npm as well as python/pip on your own.  Assuming
you have those things worked out, the installation of bower and deckmaster below
should proceed without issue.

Installation
==============

	npm install -g bower
	pip install deckmaster

Usage
=======

Switch to a directory containing a `site.json`, and execute

	deckmaster

This will run deckmaster in dev mode, and will serve the site as defined in
`site.json`.

Here's some more detail on the CLI options for deckmaster:

	$ deckmaster --help
	usage: deckmaster [-h] [--no-debug] [--workdir [WORKDIR]] [--port [PORT]]

	Serve bower packages and local assets.

	optional arguments:
	  -h, --help            show this help message and exit
	  --no-debug, -N        don't show debugger on exception or reload on file
	                        update
	  --workdir [WORKDIR], -w [WORKDIR]
	                        specify a working directory other than current
	                        directory
	  --port [PORT], -p [PORT]
	                        port to serve from

`site.json`
=============

Provides the structure of the assets served by deckmaster.

Simple example, serves only an index route of styles and scripts:

```javascript	
{
    "deps":{
    	"local":[ 
    		"static/script.js",
    		"static/style.css"
    	],
        "bower":[
    		"d3",
			"leaflet"
		]
	}
}
```

Which results in the following '/' route, served by flask:

```html
<!DOCTYPE html>
<html>
    <head>
    <meta charset="UTF-8">
    <title>title</title>
        <link rel="stylesheet" href="static/style.css" />
        <link rel="stylesheet" href="static/components/leaflet/dist/leaflet.css" />
    </head>
    <body>
        <script src="static/script.js" type="text/javascript"></script>
        <script src="static/components/d3/d3.js" type="text/javascript"></script>
        <script src="static/components/leaflet/dist/leaflet.js" type="text/javascript"></script>
    </body>
</html>
```
