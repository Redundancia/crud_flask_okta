from flask import Flask
from flask.templating import render_template
from os.path import dirname, join
from . import db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(    
    SQLALCHEMY_DATABASE_URI="sqlite:///" + join(dirname(dirname(__file__)), "database.sqlite"),)
db.init_app(app)

@app.route("/")
def index():
    """
    Render the homepage.
    """
    posts_final = []
    return render_template("blog/index.html", posts=posts_final)

@app.route("/dashboard")
def dashboard():
    """
    Render dashboard.
    """
    posts_final = []
    return render_template("blog/dashboard.html")

