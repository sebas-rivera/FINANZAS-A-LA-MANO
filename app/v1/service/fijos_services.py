from app.v1.model.fijos_model import Fijos
from app.v1.schema.fijos_schema import Fijos_Schema,Fijos2_Schema

def fijos_serv(item)-> dict:
    return {
        "Valor": item["Valor"],
        "Servicios": item["Servicios"],
        "Mobil": item["Mobil"],
        "Internet":item["Internet"],
        "Transporte":item["Transporte"],
        "Credito":item["Credito"],
        "Mes":item["Mes"],
        "user":item["user"]
    }

def save_services(FijosToday:Fijos_Schema):
    try:
        print(1)
        db_Fijos=Fijos(
            Valor= FijosToday.Valor,
            Servicios = FijosToday.Servicios,
            Mobil =  FijosToday.Mobil,
            Internet =  FijosToday.Internet,
            Transporte= FijosToday.Transporte,
            Credito=  FijosToday.Credito,
            Mes=  FijosToday.Mes,
            user=  FijosToday.user
        )
        db_Fijos.save()
        return  "Ha sido guardado exitosamente el gasto fijo del mes actual"
    except: 
        return "Ha ocurrido un error en el guardado del gasto fijo del mes actual" 

def seleccionarporusuario(ID:int):
    try:
        ListaFijos = Fijos().select().where(Fijos.user==ID).execute()
        print(type(ListaFijos))
        return list(ListaFijos)
    except:
         return []

def update_services1(FijosToday:Fijos_Schema,ID:int):
    try:
        db_Fijos=Fijos(
            Valor=FijosToday.Valor,
            Servicios=FijosToday.Servicios,
            Mobil=FijosToday.Mobil,
            Internet=FijosToday.Internet,
            Transporte=FijosToday.Transporte,
            Credito=FijosToday.Transporte,
            Mes=FijosToday.Mes,
            user = FijosToday.user
        )
        #db_Fijos.update({fijos.Valor:FijosToday,fijos.Servicios:FijosToday,fijos.Mobil:FijosToday,fijos.Internet:FijosToday,fijos.Transporte:FijosToday,fijos.Credito:FijosToday,fijos.Mes:FijosToday,fijos.user:FijosToday})
        db_Fijos.id=ID
        db_Fijos.save()

        
        return "Ha sido actualizado exitosamente la base de datos"
    except:
        return "No ha podido actualizarse exitosamente la base de datos"

def update_services(FijosToday:Fijos2_Schema,ID:int):
    try:
        row:Fijos=Fijos.get(Fijos.id==ID)
        row.Valor=FijosToday.Valor,
        row.Servicios=FijosToday.Servicios,
        row.Mobil=FijosToday.Mobil,
        row.Internet=FijosToday.Internet,
        row.Transporte=FijosToday.Transporte,
        row.Credito=FijosToday.Transporte,
        row.Mes=FijosToday.Mes,
        row.save()
        return "Ha sido actualizado exitosamente la base de datos"
    except:
        return "No ha podido actualizarse exitosamente la base de datos"


def delete_services(ID:int):
    try:
        Fijos().delete().where(Fijos.id==ID).execute()
        return "Ha sido borrado exitosamente la entrada del gasto fijo del mes actual"
    except:
        return "No ha podido eliminarse correctarmente la entrada del gasto fijo del mes actual"
       