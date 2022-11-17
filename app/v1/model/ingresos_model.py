from datetime import date
import peewee
from app.v1.utils.db import db
from .user_model import User

class Ingresos(peewee.Model):
    """Tabla para los ingresos
    """    
    Descripcion = peewee.CharField()
    Valor = peewee.IntegerField()
    Dia = peewee.DateField(default = date.today())
    user = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db