from datetime import date
import peewee
from app.v1.utils.db import db
from .user_model import User

class Fijos(peewee.Model):
    """Tabla para los gastos fijos considerados
    """    
    Valor = peewee.FloatField()
    Servicios = peewee.FloatField()
    Mobil = peewee.FloatField()
    Internet = peewee.FloatField()
    Transporte = peewee.FloatField()
    Credito = peewee.FloatField()
    Mes = peewee.DateField(default = date.today())
    user = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db