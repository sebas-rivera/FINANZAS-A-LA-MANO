from pydantic import BaseModel
from typing import Union

class Retiros_Schema(BaseModel):
    Valor:float
    Dia:str
    user: str

class Retiros2_Schema(BaseModel):
    Valor:float
    Dia:str
    