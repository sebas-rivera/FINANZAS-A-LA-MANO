import peewee
from datetime import date
from app.v1.utils.db import db
from .user_model import User

class Retiros(peewee.Model):
    """Tabla para los retiros en efectivo
    """    
    Valor = peewee.IntegerField()
    Dia = peewee.DateField(default = date.today())
    user = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db