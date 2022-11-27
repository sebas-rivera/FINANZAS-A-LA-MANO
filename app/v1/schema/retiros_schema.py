from pydantic import BaseModel
from typing import Union

class Retiros_Schema(BaseModel):
    Valor= float
    Dia= str
    user= str 

    def __init__(self,Valor,Dia,user) -> None:
        self.Valor=Valor
        self.Dia=Dia
        self.user=user

        