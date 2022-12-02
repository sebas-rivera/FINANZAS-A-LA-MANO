from app.v1.model.ingresos_model import Ingresos
from app.v1.schema.ingresos_schema import Ingresos_Schema,Ingresos2_Schema
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Se crea diccionario con las claves-valor respectivas
""" 
def ingresos_serv(item)-> dict:
    return {
        "Dia": item["Dia"],
        "Descripcion": item["Descripcion"],
        "Valor":item["Valor"],
        "user": item["user"]
    }

"""
Definimos el metodo guardar. Eventualmente será la base para el metodo post
""" 
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

"""
Definimos el metodo leer-consultar. Eventualmente será la base para el metodo get
"""     
def seleccionarporusuario(ID:int):
    try:
        ListaIngresos= Ingresos().select().where(Ingresos.user==ID).execute()
        print(type(ListaIngresos))
        return list(ListaIngresos)
    except:
        return []
  

def update_services1(Ingresostoday:Ingresos_Schema,ID:int):            
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

"""
Definimos el metodo actualizar. Eventualmente será la base para el metodo put
""" 
def update_services(Ingresostoday:Ingresos2_Schema,ID:int):            
    try:
        row:Ingresos=Ingresos.get(Ingresos.id==ID)
        row.Dia = Ingresostoday.Dia
        row.Descripcion = Ingresostoday.Descripcion
        row.Valor = Ingresostoday.Valor
        row.save()
        return "Ha sido actualizado la base de datos"
    except:
        return "No ha sido actualizado la base de datos"  

"""
Definimos el metodo eliminar. Eventualmente será la base para el metodo delete
""" 
def delete_services(ID:int):
    try:
        Ingresos().delete().where(Ingresos.id==ID).execute()
        return "Ha sido borrado exitosamente"
    except:
        return "No ha podido eliminarse correctamente"

"""
Definimos el metodo sumar. Eventualmente será la base para el retorno de imagenes
""" 
def suma(ID:int):
    try:
        query  = Ingresos().select().where(Ingresos.user==ID).execute()
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
                suma = df_pop_month.iloc[:,2]
                suma = suma.values.sum()
                valor.append(suma)
                fecha.append(str(i)+"-"+str(j))
        P = pd.DataFrame()
        P["Fecha"] = fecha
        P["Valor"] = valor
        P.plot(x='Fecha', y='Valor', kind='bar')	
        plt.savefig("Ingresos.jpg")
        return[]
    except:
         return []