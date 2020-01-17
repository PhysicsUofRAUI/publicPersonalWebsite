#
# Will contain the sqlalchemy database setup, imports, the login manager set up,
# and many other things. Bascically intiates the app for use.
#
# See the dream team example and I am sure ample documentation of how to set this
# stuff up.
#
import os

# third-party imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

# local imports
from config import app_config

db = SQLAlchemy()

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql://pwAdmin:h0ngk0ng@localhost/pw'

def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "development":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    db.init_app(app)

    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()

    bcrypt = Bcrypt(app)

    Bootstrap(app)

    from app import models

    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .other import other as other_blueprint
    app.register_blueprint(other_blueprint)

    from .photos import photos as photos_blueprint
    app.register_blueprint(photos_blueprint)

    return app
