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
from config import Config
from app.database import init_db

from app.database import db_session

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'put-your-secret-key-here'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_POOL_PRE_PING'] = True

    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 3600}

    bootstrap = Bootstrap(app)

    from app import models

    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .other import other as other_blueprint
    app.register_blueprint(other_blueprint)

    from .photos import photos as photos_blueprint
    app.register_blueprint(photos_blueprint)


    init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

        if exception and db_session.is_active:
            db_session.rollback()


    return app
