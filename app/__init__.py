import os
from flask import Flask
from app.routes.agenda_routes import agenda_bp
from flask_cors import CORS
from .extentions import db, migrate, ma
from app.models.agenda import Agenda

def create_app(config_class=None):
    app = Flask(__name__)

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config['SECRET_KEY'] = "secret"
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


    app.register_blueprint(agenda_bp)
    return app