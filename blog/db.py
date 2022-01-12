from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from click import command, echo
from datetime import datetime

db = SQLAlchemy()

@command("init-db")
@with_appcontext
def init_db_command():
    """Initialize the database."""
    db.create_all()
    echo("Database initiated.")


def init_app(app):
    """Init flask app with db."""
    db.init_app(app)
    app.cli.add_command(init_db_command)

class Post(db.Model):
    """Blog post."""
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    slug =  db.Column(db.Text, nullable=False, unique=True)
