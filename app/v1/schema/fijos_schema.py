from pydantic import BaseModel
from typing import Union
""""
Tomamos el esquema BaseModel de la libreria pydantic para definir nuestras clases.

Los atributos fueron previamente seleccionados de acuerdo con el problema a resolver,
ademas se incluye el tipo de dato que sería cada atributo
""" 
class Fijos_Schema(BaseModel):
    Valor: float
    Servicios: float
    Mobil: float
    Internet: float
    Transporte: float
    Credito: float
    Mes: str
    user: str
"""
Esta clase 2 se definio para realizar el metodo de actualizacion(put) en los archivos service 
""" 
class Fijos2_Schema(BaseModel):
    Valor: float
    Servicios: float
    Mobil: float
    Internet: float
    Transporte: float
    Credito: float
    Mes: str
    