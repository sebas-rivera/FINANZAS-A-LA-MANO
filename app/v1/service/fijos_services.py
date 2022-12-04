from app.v1.model.fijos_model import Fijos
from app.v1.schema.fijos_schema import Fijos_Schema,Fijos2_Schema
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Se crea diccionario con las claves-valor respectivas
""" 
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


"""
Definimos el metodo guardar. Eventualmente será la base para el metodo post
""" 
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

"""
Definimos el metodo leer-consultar. Eventualmente será la base para el metodo get
""" 
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

"""
Definimos el metodo actualizar. Eventualmente será la base para el metodo put
""" 
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


"""
Definimos el metodo eliminar. Eventualmente será la base para el metodo delete
""" 
def delete_services(ID:int):
    try:
        Fijos().delete().where(Fijos.id==ID).execute()
        return "Ha sido borrado exitosamente la entrada del gasto fijo del mes actual"
    except:
        return "No ha podido eliminarse correctarmente la entrada del gasto fijo del mes actual"
       


"""
Definimos el metodo sumar. Eventualmente será la base para el retorno de imagenes
""" 
def suma(ID:int):
    try:
        query  = Fijos().select().where(Fijos.user==ID)
        df = pd.DataFrame(query.dicts())
        df["year"] = pd.DatetimeIndex(df['Mes']).year
        df["month"] = pd.DatetimeIndex(df['Mes']).month
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
                suma = df_pop_month.iloc[:,1:6]
                suma = suma.values.sum()
                valor.append(suma)
                fecha.append(str(i)+"-"+str(j))
        P = pd.DataFrame()
        P["Fecha"] = fecha
        P["Valor"] = valor
        P.plot(x='Fecha', y='Valor', kind='bar')
        plt.axhline(P["Valor"].mean(), color='red', linestyle='dashed', linewidth=2)
        plt.savefig("app/v1/image/Fijos.jpg")
        file_path = os.path.join("app/v1/image/Fijos.jpg")
        return (file_path)
    except:
         return None
