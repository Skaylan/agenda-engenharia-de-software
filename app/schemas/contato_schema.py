from app.extentions import ma
from app.models.agenda import Agenda


class ContatoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Agenda
        load_instance = True
