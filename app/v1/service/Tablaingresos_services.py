from app.v1.model.ingresos_model import Ingresos
from app.v1.schema.ingresos_schema import Ingresos_Schema


def ingresos_serv(item)-> dict:
    return {
        "Dia": item["Dia"],
        "Descripcion": item["Descripcion"],
        "Valor":item["Valor"],
        "user": item["user"]
    }


def save_services(Ingresostoday:Ingresos_Schema):
  
    try:

        db_Ingresos=Ingresos(
            Dia = Ingresostoday.Dia,
            Descripcion = Ingresostoday.Descripcion,
            Valor = Ingresostoday.Valor,
            user = Ingresostoday.user
        )
        db_Ingresos.save() 
        return  "Ha sido guardado exitosamente"
    except:
        return "No ha sido guardado exitosamente"
    
  


def delete_services(ID:int):
    try:
        Ingresos().delete().where(Ingresos.id==ID).execute()
        return "Ha sido borrado exitosamente"
    except:
        return "No ha podido eliminarse correctamente"


def update_services(Ingresostoday:Ingresos_Schema,ID:int):            
    try:
        db_Ingresos=Ingresos(
            Dia = Ingresostoday.Dia,
            Descripcion = Ingresostoday.Descripcion,
            Valor = Ingresostoday.Valor,
            user = Ingresostoday.user
        )
        db_Ingresos.id=ID
        db_Ingresos.save() 

        return "Ha sido actualizado la base de datos"
    except:
        return "No ha sido actualizado la base de datos"    

def seleccionarporusuario(ID:int):
    try:
        ListaIngresos= Ingresos().select().where(Ingresos.user==ID).execute()
        print(type(ListaIngresos))
        return list(ListaIngresos)
    except:
        return []
