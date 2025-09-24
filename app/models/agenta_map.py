from app.interfaces.IAgenda import IF_Agenda
from app.interfaces.Icontato import IF_Contato
from typing import Collection, Dict, Optional
from app.models.agenda import Agenda
from app.extentions import db
from app.schemas.contato_schema import ContatoSchema

class AgendaMap(IF_Agenda):
    """Implementação da Agenda utilizando um Dicionário (Map/HashMap)."""

    def __init__(self):
        self._lista_contato: Dict[str, IF_Contato] = {}

    def adicionaContato(self, contato: IF_Contato) -> bool:
        """Adiciona um contato se o telefone não for uma chave existente no mapa."""
        telefone = Agenda.query.filter_by(telefone=contato.getTelefone()).first()

        if telefone:
            print(f"Erro: Telefone '{contato.getTelefone()}' já existe.")
            return False

        agenda = Agenda(contato.getNome(), contato.getTelefone())
        db.session.add(agenda)
        db.session.commit()

        return True

    def removeContato(self, telefone: str) -> bool:
        """Remove um contato do mapa pelo telefone (chave)."""

        contato = Agenda.query.filter_by(telefone=telefone).first()
        if not contato:
            return False

        db.session.delete(contato)
        db.session.commit()

        return True

    def getContato(self, telefone: str) -> Optional[IF_Contato]:
        """Retorna um contato do mapa pelo telefone."""
        contato = Agenda.query.filter_by(telefone=telefone).first()
        contato_schema = ContatoSchema()
        return contato_schema.dump(contato)

    def getListaAgenda(self) -> Collection[IF_Contato]:
        """Retorna todos os valores (contatos) do mapa."""
        contatos = Agenda.query.all()
        contato_schema = ContatoSchema(many=True)
        return contato_schema.dump(contatos)