from pydantic import BaseModel
from typing import Union

class Fijos_Schema(BaseModel):
    Valor: float
    Servicios: float
    Mobil: float
    Internet: float
    Transporte: float
    Credito: float
    Mes: str
    user: str
    
class Fijos2_Schema(BaseModel):
    Valor: float
    Servicios: float
    Mobil: float
    Internet: float
    Transporte: float
    Credito: float
    Mes: str
    