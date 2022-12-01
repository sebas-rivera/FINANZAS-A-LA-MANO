from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import fijos_schema
from app.v1.service import fijos_services
from app.v1.schema.fijos_schema import Fijos_Schema,Fijos2_Schema
from app.v1.utils.db import get_db

"""
Se define ruta-URL para gastos fijos
""" 
router = APIRouter(
    prefix="/api/v1/fijos",

    tags=["Fijos"]
)

"""
Se habilita la creacion de gastos fijos
""" 
@router.post(
    "/Fijos/",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo gasto fijo"
)
def create_fijos(fijos: fijos_schema.Fijos_Schema = Body(...)):

    return fijos_services.save_services(fijos)

"""
Se habilita la consulta de gastos fijos
""" 
@router.get(
    "/SeleccionarporID/",
    status_code=status.HTTP_200_OK,
    response_model=list,
    dependencies=[Depends(get_db)],
    summary="selecciona por Usuario"
)
def seleccionarporusuario(ID:int):
    
    return fijos_services.seleccionarporusuario(ID)

"""
Se habilita la actualizacion de gastos fijos
""" 

@router.put(
    "/Actualizar/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Actualiza el gasto fijo"
)
def put_fijos(ID:int,fijos: fijos_schema.Fijos2_Schema = Body(...)):

    return fijos_services.update_services(fijos,ID)

"""
Se habilita la eliminacion de gastos fijos
""" 
@router.delete(
    "/Delete/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Elimina el gasto fijo creado anteriormente"
)
def delete_fijos(ID:int):

    return fijos_services.delete_services(ID)
