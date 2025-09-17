from app.interfaces.IAgenda import IF_Agenda
from app.interfaces.Icontato import IF_Contato
from typing import Collection, Dict, Optional

class AgendaMap(IF_Agenda):
    """Implementação da Agenda utilizando um Dicionário (Map/HashMap)."""

    def __init__(self):
        self._lista_contato: Dict[str, IF_Contato] = {}

    def adicionaContato(self, contato: IF_Contato) -> bool:
        """Adiciona um contato se o telefone não for uma chave existente no mapa."""
        telefone = contato.getTelefone()
        if telefone in self._lista_contato:
            print(f"Erro: Telefone '{telefone}' já existe.")
            return False
        self._lista_contato[telefone] = contato
        return True

    def removeContato(self, telefone: str) -> bool:
        """Remove um contato do mapa pelo telefone (chave)."""
        if telefone in self._lista_contato:
            del self._lista_contato[telefone]
            return True
        return False

    def getContato(self, telefone: str) -> Optional[IF_Contato]:
        """Retorna um contato do mapa pelo telefone."""
        return self._lista_contato.get(telefone)

    def getListaAgenda(self) -> Collection[IF_Contato]:
        """Retorna todos os valores (contatos) do mapa."""
        return self._lista_contato.values()