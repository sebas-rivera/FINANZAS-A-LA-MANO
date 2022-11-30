from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import retiros_schema
from app.v1.service import retiros_services
from app.v1.schema.retiros_schema import Retiros_Schema,Retiros2_Schema
from app.v1.utils.db import get_db

router = APIRouter(
    prefix="/api/v1/retiros",
    
    tags=["Retiros"]
)

@router.post(
    "/Retiros/",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo ingreso"
)
def create_retiros(retiros: retiros_schema.Retiros_Schema = Body(...)):

    return retiros_services.save_services(retiros)

@router.get(
    "/SeleccionarporID/",
    status_code=status.HTTP_200_OK,
    response_model=list,
    dependencies=[Depends(get_db)],
    summary="selecciona por Usuario"
)
def seleccionarporusuario(ID:int):

    return retiros_services.seleccionarporusuario(ID)
    

@router.put(
    "/Actualizar/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Actualiza el ingreso"
)
def put_retiros(ID:int,retiros: retiros_schema.Retiros2_Schema = Body(...)):

    return retiros_services.update_services(retiros,ID)

@router.delete(
    "/Delete/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Elimina el ingreso creado anteriormente"
)
def delete_retiros(ID:int):

    return retiros_services.delete_services(ID)
