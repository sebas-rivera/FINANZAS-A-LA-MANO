from pydantic import BaseModel
from typing import Optional
""""
Tomamos el esquema BaseModel de la libreria pydantic para definir nuestras clases.

Los atributos fueron previamente seleccionados de acuerdo con el problema a resolver,
ademas se incluye el tipo de dato que sería cada atributo
""" 

class Token(BaseModel):
    access_token: str
    token_type: str

"""
Estos token permite la autorizacion y seguridad de los usuarios
"""

class TokenData(BaseModel):
    username: Optional[str] = None