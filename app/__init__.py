from flask import Flask
from app.routes.agenda_routes import agenda_bp
from flask_cors import CORS

def create_app(config_class=None):
    app = Flask(__name__)
    app.register_blueprint(agenda_bp)
    CORS(app)


    return app