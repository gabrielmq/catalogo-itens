#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config


db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.api import blue_print as api
    app.register_blueprint(api)

    from app.controllers.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from app.controllers.categoria import categ as categoria_bp
    app.register_blueprint(categoria_bp)

    return app


import app.models.model
