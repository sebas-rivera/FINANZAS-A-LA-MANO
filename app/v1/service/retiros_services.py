from app.v1.model.retiros_model import Retiros
from app.v1.schema.retiros_schema import Retiros_Schema,Retiros2_Schema
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Se crea diccionario con las claves-valor respectivas
""" 
def retiros_serv(item)-> dict:
    return{
        "Valor": item["Valor"],
        "Dia": item["Dia"],
        "user": item["item"]
    }

"""
Definimos el metodo guardar. Eventualmente será la base para el metodo post
""" 
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

"""
Definimos el metodo leer-consultar. Eventualmente será la base para el metodo get
""" 
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
"""
Definimos el metodo actualizar. Eventualmente será la base para el metodo put
""" 
def update_services(RetirosToday:Retiros2_Schema,ID:int):            
    try:
        row:Retiros=Retiros.get()
        row.Valor = RetirosToday.Valor
        row.Dia = RetirosToday.Dia
        row.save()
        return "Ha sido actualizado la base de datos"
    except:
        return "No ha sido actualizado la base de datos" 

"""
Definimos el metodo eliminar. Eventualmente será la base para el metodo delete
""" 
def delete_services(ID:int):
    try:
        Retiros().delete().where(Retiros.id==ID).execute()
        return "Ha sido borrado exitosamente"
    except:
        return "No ha podido eliminarse correctamente"

"""
Definimos el metodo sumar. Eventualmente será la base para el retorno de imagenes
""" 
def suma(ID:int):
    try:
        query  = Retiros().select().where(Retiros.user==ID).execute()
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
        plt.savefig("Retiros.jpg")
        return[]
    except:
         return []