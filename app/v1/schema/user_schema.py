from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
""""
Tomamos el esquema BaseModel de la libreria pydantic para definir nuestras clases.

Los atributos fueron previamente seleccionados de acuerdo con el problema a resolver,
ademas se incluye el tipo de dato que sería cada atributo
""" 
class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="minombre@email.com"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Nombre_Apellido"
    )

"""
Estas clases se defininen para la recepción de la información ejemplificacion del formto de la base de datos
"""

class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )

class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="Contrasena1234"
    )