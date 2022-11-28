from pydantic import BaseModel
from typing import Union

class Variables_Schema(BaseModel):
    Descripcion:str
    Valor:float
    Credito:bool
    Debito: bool
    Efectivo:bool
    Dia:str
    user:str


    