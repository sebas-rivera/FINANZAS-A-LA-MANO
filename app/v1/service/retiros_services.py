from app.v1.model.retiros_model import Retiros
from app.v1.schema.retiros_schema import Retiros_Schema,Retiros2_Schema

def retiros_serv(item)-> dict:
    return{
        "Valor": item["Valor"],
        "Dia": item["Dia"],
        "user": item["item"]
    }

def save_services(RetirosToday:Retiros_Schema):
  
    try:

        db_Retiros=Retiros(
            Valor = RetirosToday.Valor,
            Dia = RetirosToday.Dia,
            user = RetirosToday.user
        )
        db_Retiros.save() 
        return  "Ha sido guardado exitosamente"
    except:
        return "No ha sido guardado exitosamente"

def seleccionarporusuario(ID:int):
    try:
        ListaRetiros= Retiros().select().where(Retiros.user==ID).execute()
        print(type(ListaRetiros))
        return list(ListaRetiros)
    except:
        return []

def update_services1(RetirosToday:Retiros_Schema,ID:int):            
    try:
        db_Retiros=Retiros(
            Valor = RetirosToday.Valor,
            Dia = RetirosToday.Dia,
            user = RetirosToday.user,
        )
        db_Retiros.id=ID
        db_Retiros.save() 

        return "Ha sido actualizado la base de datos"
    except:
        return "No ha sido actualizado la base de datos"   

def update_services(RetirosToday:Retiros2_Schema,ID:int):            
    try:
        row:Retiros=Retiros.get()
        row.Valor = RetirosToday.Valor
        row.Dia = RetirosToday.Dia
        row.save()
        return "Ha sido actualizado la base de datos"
    except:
        return "No ha sido actualizado la base de datos" 

def delete_services(ID:int):
    try:
        Retiros().delete().where(Retiros.id==ID).execute()
        return "Ha sido borrado exitosamente"
    except:
        return "No ha podido eliminarse correctamente"

        
