from flask import Blueprint
from app.controllers.agenda_controller import AgendaController


agenda_bp = Blueprint('agenda_routes', __name__)


@agenda_bp.post('/api/v1/adicionar_contato')(AgendaController.adicionar_contato)


def register_routes(app):
    app.register_blueprint(agenda_bp, url_prefix="/api")