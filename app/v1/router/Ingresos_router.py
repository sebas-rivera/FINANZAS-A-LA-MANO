from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import ingresos_schema
from app.v1.service import ingresos_services
from app.v1.service import ingresos_services
from app.v1.schema.ingresos_schema import Ingresos_Schema,Ingresos2_Schema
from app.v1.utils.db import get_db
import os


"""
Se define ruta para gastos ingresos
""" 
router = APIRouter(
    prefix="/api/v1/ingresos",
    
    tags=["Ingresos"]
)

"""
Se habilita la creacion de ingresos
""" 
@router.post(
    "/Ingresos/",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo ingreso"
)
def create_ingresos(ingresos: ingresos_schema.Ingresos_Schema = Body(...)):

    return ingresos_services.save_services(ingresos)

"""
Se habilita la consulta de ingresos
""" 
@router.get(
    "/SeleccionarporID/",
    status_code=status.HTTP_200_OK,
    response_model=list,
    dependencies=[Depends(get_db)],
    summary="selecciona por Usuario"
)
def seleccionarporusuario(ID:int):

    return ingresos_services.seleccionarporusuario(ID)

"""
Se habilita la actualizacion de ingresos
""" 

@router.put(
    "/Actualizar/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Actualiza el ingreso"
)
def put_ingresos(ID:int,ingresos: ingresos_schema.Ingresos2_Schema = Body(...)):

    return ingresos_services.update_services(ingresos,ID)

"""
Se habilita la eliminacion de ingresos
""" 
@router.delete(
    "/Delete/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Elimina el ingreso creado anteriormente"
)
def delete_ingresos(ID:int):

    return ingresos_services.delete_services(ID)

"""
Se habilita creacion de imagenes de ingresos
""" 
@router.get(
    "/Imagen/",
    responses={200: {"description": "Grafica de sus gastos"}}
)
def Imagen(ID:int):
    file_path = ingresos_services.suma(ID)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg", filename="Ingresos.jpg")
    return {"error" : "File not found!"}