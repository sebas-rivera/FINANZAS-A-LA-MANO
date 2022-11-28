from pydantic import BaseModel
from typing import Union

class Ingresos_Schema(BaseModel):
    Dia:str
    Descripcion:str
    Valor: float
    user:str


