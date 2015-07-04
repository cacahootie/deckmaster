"""deckmaster app"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
    	'html/base.html',
    	styles = ['/static/style.css',],
    	scripts = ['/static/script.js',],
    )

