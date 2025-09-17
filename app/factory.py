from app.models.agenta_map import AgendaMap
from app.models.contato import AgendaList
from app.interfaces.IAgenda import IF_Agenda

class FabricaAgenda:
    """
    Classe que implementa os padrões Singleton e Factory Method para criar
    objetos do tipo IF_Agenda.
    """
    AGENDAMAP = 0
    AGENDALIST = 1

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FabricaAgenda, cls).__new__(cls)
        return cls._instance

    def criaAgenda(self, tipo: int) -> IF_Agenda:
        """
        Método Factory que cria e retorna uma instância de uma agenda
        com base no tipo fornecido.
        """
        if tipo == self.AGENDAMAP:
            return AgendaMap()
        elif tipo == self.AGENDALIST:
            return AgendaList()
        else:
            raise ValueError("Tipo de agenda desconhecido.")

# Singleton: instância única da fábrica para ser usada em toda a aplicação
fabrica_agenda = FabricaAgenda()