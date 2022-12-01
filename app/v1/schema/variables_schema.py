from pydantic import BaseModel
from typing import Union
""""
Tomamos el esquema BaseModel de la libreria pydantic para definir nuestras clases.

Los atributos fueron previamente seleccionados de acuerdo con el problema a resolver,
ademas se incluye el tipo de dato que sería cada atributo
""" 
class Variables_Schema(BaseModel):
    Descripcion:str
    Valor:float
    Credito:bool
    Debito: bool
    Efectivo:bool
    Dia:str
    user:str
"""
Esta clase 2 se definio para realizar el metodo de actualizacion(put) en los archivos service 
""" 
class Variables2_Schema(BaseModel):
    Descripcion:str
    Valor:float
    Credito:bool
    Debito: bool
    Efectivo:bool
    Dia:str
    

    