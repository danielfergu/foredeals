import sys
import os
sys.path.append('src/applications/')
sys.path.append('src/applications/web_app/')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.environment import Environment
from web_app.index_page import index_page
from web_app.notification_page import notification_page
from web_app.health_api import health_api
from web_app.models import db

def create_app(env: Environment = Environment.from_env(), testing: bool = False) -> Flask:
    app = Flask(__name__)
    #app.secret_key = env.secret_key

    if testing:
        # Configure the app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        # Configure the app for production/development
        app.config['SQLALCHEMY_DATABASE_URI'] = env.database_url
        #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)
    if not testing:
        # Only initialize Migrate if not in testing mode
        migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(index_page())
    app.register_blueprint(notification_page())
    app.register_blueprint(health_api())

    return app
