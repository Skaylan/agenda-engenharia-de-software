from abc import ABC, abstractmethod
from app.interfaces.Icontato import IF_Contato
from typing import Collection, Optional
class IF_Agenda(ABC):
    """Interface que define as operações de uma Agenda."""

    @abstractmethod
    def adicionaContato(self, contato: IF_Contato) -> bool:
        """Adiciona um novo contato na agenda."""
        pass

    @abstractmethod
    def removeContato(self, telefone: str) -> bool:
        """Remove um contato da agenda pelo telefone."""
        pass

    @abstractmethod
    def getContato(self, telefone: str) -> Optional[IF_Contato]:
        """Localiza e retorna um contato pelo telefone."""
        pass

    @abstractmethod
    def getListaAgenda(self) -> Collection[IF_Contato]:
        """Retorna a lista de todos os contatos da agenda."""
        pass