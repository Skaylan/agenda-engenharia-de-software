from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, Integer, String
from app.extentions import Base


class Agenda(Base):
    __tablename__ = "Agenda"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(Text, unique=False, nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    def __init__(self, nome:str, telefone:str):
        self.nome = nome
        self.telefone = telefone