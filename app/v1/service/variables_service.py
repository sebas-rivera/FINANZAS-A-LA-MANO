from app.v1.model.variables_model import  Variables
from app.v1.schema.variables_schema import Variables_Schema,Variables2_Schema


"""
Se crea diccionario con las claves-valor respectivas
""" 
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

"""
Definimos el metodo guardar. Eventualmente será la base para el metodo post
""" 
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

"""
Definimos el metodo leer-consultar. Eventualmente será la base para el metodo get
"""         
def seleccionarporusuario(ID:int):
    try:
        Listavariables= Variables().select().where(Variables.user==ID).execute()
        print(type(Listavariables))
        return list(Listavariables)
    except:
        return []



def update_services1(VariablesToday:Variables_Schema,ID:int):
    try:
        #Este es el constructor de las filas de la tabla variables 
        db_variables=Variables(
            Valor=VariablesToday.Valor,
            Credito=VariablesToday.Credito,
            Debito=VariablesToday.Debito,
            Efectivo=VariablesToday.Efectivo,
            Dia=VariablesToday.Dia,
            user=VariablesToday.user
        )
        db_variables.id=ID
        db_variables.save()

        #variables.update({variables.Valor:VariablesToday,variables.Credito:VariablesToday,variables.Debito:VariablesToday,variables.Efectivo:VariablesToday,variables.Dia:VariablesToday,variables.user:VariablesToday,})

        return "Ha sido actualizado exitosamente la base de datos"
    except:
        return "No ha podido actualizarse exitosamente la base de datos"

"""
Definimos el metodo actualizar. Eventualmente será la base para el metodo put
""" 
def update_services(VariablesToday:Variables2_Schema,ID:int):
    try:

        #Variables().update({variables.Valor:VariablesToday,variables.Credito:VariablesToday,variables.Debito:VariablesToday,variables.Efectivo:VariablesToday,variables.Dia:VariablesToday,variables.user:VariablesToday,})
        #query = Tweet.update(is_published=True).where(Tweet.creation_date < today)
        row:Variables=Variables.get(Variables.id==ID) 
        row.Descripcion=VariablesToday.Descripcion
        row.Valor=VariablesToday.Valor
        row.Credito=VariablesToday.Credito
        row.Debito=VariablesToday.Debito
        row.Efectivo=VariablesToday.Efectivo
        row.Dia=VariablesToday.Dia
        row.save()
        return "Ha sido actualizado exitosamente la base de datos"
    except:
        return "No ha podido actualizarse exitosamente la base de datos"

"""
Definimos el metodo eliminar. Eventualmente será la base para el metodo delete
""" 
def delete_services(ID:int):
    try:
        Variables().delete().where(Variables.id==ID).execute()
        return "Ha sido borrado correctamente"
    except:
        return "No ha podido eliminarse correctamente"

