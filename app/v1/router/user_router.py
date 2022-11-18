from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.service import auth_service
from app.v1.schema.token_schema import Token
from app.v1.utils.db import get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["users"]
)

@router.post(
    "/user/",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo usuario"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Crea un nuevo usuario en la app

    ### Args
    La aplicación puede recibir los siguientes campos en un JSON
    - email: Un correo valido
    - username: Nombre de usuario unico
    - password: Clave para la autenticacion

    ### Returns
    - user: Informacion de usuario
    """
    return user_service.create_user(user)

@router.post(
    "/login",
    tags=["users"],
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Iniciar sesión para el token de acceso

    ### Args
    La aplicación puede recibir los siguientes campos por datos de formulario
    - username: Tu usuario o email
    - password: Tu clave

    ### Returns
    - token de acceso y tipo de token
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")