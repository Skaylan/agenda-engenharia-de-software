from flask import Blueprint
from app.controllers.agenda_controller import AgendaController


agenda_bp = Blueprint('agenda_routes', __name__)

agenda_bp.add_url_rule(
    "/api/v1/adicionar_contato",
    view_func=AgendaController.adicionar_contato,
    methods=["POST"]
)

agenda_bp.add_url_rule(
    "/api/v1/localizar_contato",
    view_func=AgendaController.localizar_contato,
    methods=["GET"]
)

agenda_bp.add_url_rule(
    "/api/v1/remover_contato",
    view_func=AgendaController.remover_contato,
    methods=["DELETE"]
)

agenda_bp.add_url_rule(
    "/api/v1/listar_contatos",
    view_func=AgendaController.listar_contatos,
    methods=["GET"]
)

# @agenda_bp.post('/api/v1/adicionar_contato')(AgendaController.adicionar_contato)


def register_routes(app):
    app.register_blueprint(agenda_bp, url_prefix="/api")