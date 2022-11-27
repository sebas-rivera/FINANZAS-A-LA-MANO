from pydantic import BaseModel
from typing import Union

class Fijos_Schema(BaseModel):
    Valor= float
    Servicios= float
    Mobil= float
    Internet= float
    Transporte= float
    Credito= float
    Mes= str
    user= str

    def __ini__(self,Valor,Servicios,Mobil,Internet,Transporte,Credito,Mes,user)-> None:
        self.Valor=Valor
        self.Servicios=Servicios
        self.Mobil=Mobil
        self.Internet=Internet
        self.Transporte=Transporte
        self.Credito=Credito
        self.Mes=Mes
        self.user=user
    