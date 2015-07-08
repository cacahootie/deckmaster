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

Simple Case
------------

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

Multiple Routes
----------------

Of course, when is life ever as simple as one single index route?  Rarely.
deckmaster of course supports multiple routes, defined as such:

```json
{
    "/":{
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
    },
    "/a":{
        "deps":{
            "bower":[
                "jquery",
                "underscore"
            ]
        }
    },
    "/b":{
        "deps":{
            "local":[
                "static/script.js",
                "static/style.css"
            ]
        }
    }
}
```

Which will produce html at the respective paths according to the packages
included.

Bower Package --> Script Tag
=============================

Each `bower.json` for a given package provides a `main` value, which according
to the bower specification, should include at most one file of each file type
which serves as an entry point to the package, be it `.js` or `.css`, `.scss` or
`.whocaresicertainlydont`.  The problem is that this isn't enforced, so 
deckmaster resolves the issue by allowing one script and one style from each
package, which is either the single file provided, or in the case of an array,
it prefers the first file of each type specified.  deckmaster currently only
handles styles and scripts of type `.css` and `.js`.
