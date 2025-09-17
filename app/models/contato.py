from typing import Collection, Dict, List, Optional
from app.interfaces.IAgenda import IF_Agenda
from app.interfaces.Icontato import IF_Contato

class Contato(IF_Contato):
    """Implementação concreta da classe Contato."""

    def __init__(self, nome: str, telefone: str):
        if not nome or not telefone:
            raise ValueError("Nome e telefone não podem ser vazios.")
        self._nome = nome
        self._telefone = telefone

    def getNome(self) -> str:
        return self._nome

    def getTelefone(self) -> str:
        return self._telefone

    def setNome(self, nome: str) -> None:
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = nome

    def setTelefone(self, telefone: str) -> None:
        if not telefone:
            raise ValueError("Telefone não pode ser vazio.")
        self._telefone = telefone

class AgendaList(IF_Agenda):
    """Implementação da Agenda utilizando uma Lista (List)."""

    def __init__(self):
        self._lista_contato: List[IF_Contato] = []

    def _localizaContato(self, telefone: str) -> int:
        """Método privado para encontrar o índice de um contato pelo telefone."""
        for i, contato in enumerate(self._lista_contato):
            if contato.getTelefone() == telefone:
                return i
        return -1

    def adicionaContato(self, contato: IF_Contato) -> bool:
        """Adiciona um contato se o telefone não existir na lista."""
        if self.getContato(contato.getTelefone()):
            print(f"Erro: Telefone '{contato.getTelefone()}' já existe.")
            return False
        self._lista_contato.append(contato)
        return True

    def removeContato(self, telefone: str) -> bool:
        """Remove um contato da lista pelo telefone."""
        index = self._localizaContato(telefone)
        if index != -1:
            self._lista_contato.pop(index)
            return True
        return False

    def getContato(self, telefone: str) -> Optional[IF_Contato]:
        """Retorna um contato da lista pelo telefone."""
        index = self._localizaContato(telefone)
        if index != -1:
            return self._lista_contato[index]
        return None

    def getListaAgenda(self) -> Collection[IF_Contato]:
        """Retorna todos os contatos da agenda."""
        return self._lista_contato