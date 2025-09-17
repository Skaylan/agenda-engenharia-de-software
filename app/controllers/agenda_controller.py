from flask import jsonify, request
from app.factory import fabrica_agenda, FabricaAgenda
from app.models.contato import Contato
from app.interfaces.IAgenda import IF_Contato

# Utilizando a fábrica para criar uma agenda do tipo Mapa.
# Para usar a implementação com lista, mude para FabricaAgenda.AGENDALIST.
agenda = fabrica_agenda.criaAgenda(FabricaAgenda.AGENDAMAP)


class AgendaController:

    @staticmethod
    def adicionar_contato():
        """Endpoint para adicionar um novo contato."""
        dados = request.get_json()
        if not dados or 'nome' not in dados or 'telefone' not in dados:
            return jsonify({"erro": "Dados incompletos (requer 'nome' e 'telefone')."}), 400

        try:
            contato = Contato(dados['nome'], dados['telefone'])
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

        if agenda.adicionaContato(contato):
            return jsonify({
                "mensagem": "Contato adicionado com sucesso.",
                "contato": {"nome": contato.getNome(), "telefone": contato.getTelefone()}
            }), 201
        else:
            return jsonify({"erro": f"Contato com telefone {contato.getTelefone()} já existe."}), 409

    @staticmethod
    def localizar_contato():
        """Endpoint para localizar um contato pelo telefone."""

        telefone = request.args.get('telefone')
        if not telefone:
            return jsonify({"erro": "Telefone obrigatório."}), 400

        contato = agenda.getContato(telefone)
        if contato:
            return jsonify({"nome": contato.getNome(), "telefone": contato.getTelefone()}), 200
        else:
            return jsonify({"erro": "Contato não encontrado."}), 404


    @staticmethod
    def remover_contato():
        """Endpoint para remover um contato pelo telefone."""

        dados = request.get_json()
        if not dados or 'telefone' not in dados:
            return jsonify({"erro": "Telefone obrigatório."}), 400

        telefone = dados['telefone']

        if agenda.removeContato(telefone):
            return jsonify({"mensagem": "Contato removido com sucesso."}), 200
        else:
            return jsonify({"erro": "Contato não encontrado."}), 404

    @staticmethod
    def listar_contatos():
        """Endpoint para listar todos os contatos."""
        lista_de_contatos = agenda.getListaAgenda()
        contatos_json = [
            {"nome": c.getNome(), "telefone": c.getTelefone()} for c in lista_de_contatos
        ]
        return jsonify(contatos_json), 200
