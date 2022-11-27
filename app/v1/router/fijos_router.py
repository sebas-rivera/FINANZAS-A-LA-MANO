from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from app.v1.schema import fijos_schema
from app.v1.service import fijos_services
from app.v1.service import fijos_services
from app.v1.schema.fijos_schema import Fijos_Schema
from app.v1.utils.db import get_db

router = APIRouter(
    prefix="/api/v1/fijos",

    tags=["Fijos"]
)

@router.post(
    "/Fijos/",
    status_code=status.HTTP_201_CREATED,
    response_model=fijos_schema.Fijos_Schema,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo gasto fijo"
)
def create_fijos(fijos: fijos_schema.Fijos_Schema = Body(...)):

    return fijos_schema.save_services(fijos)



