from pydantic import BaseModel
from typing import Union

""""
Tomamos el esquema BaseModel de la libreria pydantic para definir nuestras clases.

Los atributos fueron previamente seleccionados de acuerdo con el problema a resolver,
ademas se incluye el tipo de dato que sería cada atributo
""" 
class Ingresos_Schema(BaseModel):
    Dia:str
    Descripcion:str
    Valor: float
    user:str
"""
Esta clase 2 se definio para realizar el metodo de actualizacion(put) en los archivos service 
""" 
class Ingresos2_Schema(BaseModel):
    Dia:str
    Descripcion:str
    Valor: float


