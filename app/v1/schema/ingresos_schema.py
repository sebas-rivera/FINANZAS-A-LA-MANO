from pydantic import BaseModel
from typing import Union

class Ingresos_Schema(BaseModel):
    Dia:str
    Descripcion: Union[str, None]=None
    Valor: float
    user:str
    """
    def __init__(self,Dia,Descripcion,Valor,user) -> None:
        self.Dia=Dia
        self.Descripcion=Descripcion
        self.Valor=Valor
        self.user=user
    """
  



   



