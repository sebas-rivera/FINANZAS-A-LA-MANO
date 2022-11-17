from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.utils.db import get_db

router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)

def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Crea un nuevo usuario en la app

    ### Args
    La aplicación puede recibir campos de texto en un JSON
    - email: Correo valido
    - username: Nombre de usuario inexistente
    - password: Clave para la autenticacion

    ### Returns
    - user: Informacion de usuario
    """
    return user_service.create_user(user)