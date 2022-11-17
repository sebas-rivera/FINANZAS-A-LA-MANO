from app.v1.model.user_model import User
from app.v1.model.fijos_model import Fijos
from app.v1.model.variables_model import Variables
from app.v1.model.retiros_model import Retiros
from app.v1.model.ingresos_model import Ingresos
from app.v1.utils.db import db

def create_tables()-> None:
    """Funcion para crear las tablas en la base de datos de postgresql
    """    
    with db:
        db.create_tables([User, Fijos, Variables, Retiros, Ingresos])