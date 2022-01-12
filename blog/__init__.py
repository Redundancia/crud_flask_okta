from flask import Flask, g
from flask.templating import render_template
from os.path import dirname, join
from . import db, auth

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(
    SECRET_KEY="just_a_test_take_it_not_gonna_bother_hiding_it",
    OIDC_CLIENT_SECRETS=join(dirname(dirname(__file__)), "client_secrets.json"),
    OIDC_COOKIE_SECURE=False,
    OIDC_CALLBACK_ROUTE="/oidc/callback",
    OIDC_SCOPES=["openid", "email", "profile"],
    OIDC_ID_TOKEN_COOKIE_NAME="oidc_token",
    SQLALCHEMY_DATABASE_URI="sqlite:///" + join(dirname(dirname(__file__)), "database.sqlite"),
)

auth.oidc.init_app(app)
db.init_app(app)
app.register_blueprint(auth.bp)

@app.before_request
def before_request():
    """
    Load a user object into `g.user` before each request.
    """
    if auth.oidc.user_loggedin:
        g.user = auth.okta_client.get_user(auth.oidc.user_getfield("sub"))
    else:
        g.user = None

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

