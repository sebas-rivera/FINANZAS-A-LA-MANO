from pydantic import BaseModel
from typing import Union

class Variables_Schema(BaseModel):
    Valor:float
    Credito:str
    Debito: str
    Efectivo:str
    Dia:str
    user:str

    def __init__(self,Valor,Credito,Debito,Efectivo,Dia,user) -> None:
        self.Valor=Valor
        self.Credito=Credito
        self.Debito=Debito
        self.Efectivo=Efectivo
        self.Dia=Dia
        self.user=user



    