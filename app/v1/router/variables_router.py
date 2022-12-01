from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import variables_schema
from app.v1.service import variables_service
from app.v1.service import variables_service
from app.v1.schema.variables_schema import Variables_Schema,Variables2_Schema
from app.v1.utils.db import get_db

"""
Se define ruta para gastos variables
""" 

router = APIRouter(
    prefix="/api/v1/variables",
    
    tags=["Variables"]
)

"""
Se habilita la creacion de gastos variables
""" 
@router.post(
    "/Variables/",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo gasto variable"
)
def create_ingresos(variables: variables_schema.Variables_Schema= Body(...)):

    return variables_service.save_services(variables)

"""
Se habilita la consulta de gastos variables
""" 
@router.get(
    "/SeleccionarporID/",
    status_code=status.HTTP_200_OK,
    response_model=list,
    dependencies=[Depends(get_db)],
    summary="selecciona por Usuario"
)
def seleccionarporusuario(ID:int):

    return variables_service.seleccionarporusuario(ID)


"""
Se habilita la actualizacion de gastos variables
""" 
@router.put(
    "/Actualizar/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Actualiza el ingreso"
)
def put_variables(ID:int,variables:variables_schema.Variables2_Schema = Body(...)):

    return variables_service.update_services(variables,ID)

"""
Se habilita la eliminacion de gastos variables
""" 
@router.delete(
    "/Delete/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    dependencies=[Depends(get_db)],
    summary="Elimina el ingreso creado anteriormente"
)
def delete_ingresos(ID:int):

    return variables_service.delete_services(ID)
