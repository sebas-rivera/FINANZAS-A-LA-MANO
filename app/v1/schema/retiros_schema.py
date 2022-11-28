from pydantic import BaseModel
from typing import Union

class Retiros_Schema(BaseModel):
    Valor:float
    Dia:str
    user: str