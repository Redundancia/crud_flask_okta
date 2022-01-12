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