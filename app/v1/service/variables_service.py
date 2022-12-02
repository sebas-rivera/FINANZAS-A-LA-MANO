from app.v1.model.variables_model import  Variables
from app.v1.schema.variables_schema import Variables_Schema,Variables2_Schema
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

"""
Definimos el metodo sumar. Eventualmente será la base para el retorno de imagenes
""" 
def suma(ID:int):
    try:
        query  = Variables().select().where(Variables.user==ID).execute()
        df = pd.DataFrame(query.dicts())
        df["year"] = pd.DatetimeIndex(df['Dia']).year
        df["month"] = pd.DatetimeIndex(df['Dia']).month
        year = pd.unique(df['year'])
        year = year.tolist()
        year.sort()
        month = pd.unique(df['month'])
        month = month.tolist()
        month.sort()
        fecha = []
        valor = []
        for i in year:
            df_pop_year = df.loc[df['year']==i]
            for j in month:
                pass
                df_pop_month = df_pop_year.loc[df['month']==j]
                suma = df_pop_month.iloc[:,2]
                suma = suma.values.sum()
                valor.append(suma)
                fecha.append(str(i)+"-"+str(j))
        P = pd.DataFrame()
        P["Fecha"] = fecha
        P["Valor"] = valor
        P.plot(x='Fecha', y='Valor', kind='bar')	
        plt.savefig("Variables.jpg")
        return[]
    except:
         return []