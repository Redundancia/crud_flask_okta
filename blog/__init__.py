from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the homepage.
    """
    posts_final = []
    return render_template("blog/index.html", posts=posts_final)