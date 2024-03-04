"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    for i in df.columns:
        
        try:
            df[i] = df[i].str.lower().str.strip()
        except:
            pass

    df["barrio"] = df["barrio"].str.replace(r'[^a-zA-Z0-9]', '')
    
    df["fecha_de_beneficio"] = pd.to_datetime(df['fecha_de_beneficio'], 
                                              format='%d/%m/%Y', 
                                              errors='coerce')
    
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].fillna(pd.to_datetime(df['fecha_de_beneficio'], 
                                                                              format='%Y/%m/%d', errors='coerce'))

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(r'[^a-zA-Z0-9]', '')
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    print(df)

    #
    # Inserte su código aquí
    #

    return df

clean_data()
