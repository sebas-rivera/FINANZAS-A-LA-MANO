from app.v1.model.variables_model import  Variables
from app.v1.schema.variables_schema import Variables_Schema



def variables_serv(item)-> dict:
    return {
        "Descripcion": item["Descripcion"],
        "Valor": item["Valor"],
        "Credito": item["Credito"],
        "Debito": item["Debito"],
        "Efectivo": item["Efectivo"],
        "Dia": item["Dia"],
        "user": item["user"]
    }


def save_services(VariablesToday:Variables_Schema):
    try:
        db_variables= Variables(
        Descripcion=VariablesToday.Descripcion,   
        Valor= VariablesToday.Valor,
        Credito = VariablesToday.Credito,
        Debito =  VariablesToday.Debito,
        Efectivo =  VariablesToday.Efectivo,
        Dia= VariablesToday.Dia,
        user=  VariablesToday.user
        )
        db_variables.save()
        return  "Ha sido guardado exitosamente el gasto fijo del mes actual"
    except:
        return "No ha sido guardado "
        

def delete_services(ID:int):
    try:
        Variables().delete().where(Variables.id==ID).execute()
        return "Ha sido borrado correctamente"
    except:
        return "No ha podido eliminarse correctamente"

def update_services(VariablesToday:Variables_Schema,ID:int):
    try:
        variables=Variables()
        variables.update({variables.Valor:VariablesToday,variables.Credito:VariablesToday,variables.Debito:VariablesToday,variables.Efectivo:VariablesToday,variables.Dia:VariablesToday,variables.user:VariablesToday,})

        return "Ha sido actualizado exitosamente la base de datos"
    except:
        return "No ha podido actualizarse exitosamente la base de datos"

def seleccionarporusuario(ID:int):
    try:
        Listavariables= Variables().select().where(Variables.user==ID).execute()
        print(type(Listavariables))
        return list(Listavariables)
    except:
        return []
