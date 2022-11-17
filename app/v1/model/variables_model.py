from datetime import date
import peewee
from app.v1.utils.db import db
from .user_model import User

class Variables(peewee.Model):
    """Tabla para los gastos variables
    """    
    Descripcion = peewee.CharField()
    Valor = peewee.FloatField()
    Credito = peewee.BooleanField(default=False)
    Debito = peewee.BooleanField(default=False)
    Efectivo = peewee.BooleanField(default=False)
    Dia = peewee.DateField(default = date.today())
    user = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db