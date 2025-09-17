from abc import ABC, abstractmethod
from typing import Collection, Optional

class IF_Contato(ABC):
    """Interface que define os métodos para um Contato."""

    @abstractmethod
    def getNome(self) -> str:
        """Retorna o nome do contato."""
        pass

    @abstractmethod
    def getTelefone(self) -> str:
        """Retorna o telefone do contato."""
        pass

    @abstractmethod
    def setNome(self, nome: str) -> None:
        """Define o nome do contato."""
        pass

    @abstractmethod
    def setTelefone(self, telefone: str) -> None:
        """Define o telefone do contato."""
        pass

    def __eq__(self, other):
        """Compara dois contatos pelo telefone."""
        if not isinstance(other, IF_Contato):
            return NotImplemented
        return self.getTelefone() == other.getTelefone()

    def __str__(self) -> str:
        """Retorna uma representação em string do contato."""
        return f"Nome: {self.getNome()}, Telefone: {self.getTelefone()}"
