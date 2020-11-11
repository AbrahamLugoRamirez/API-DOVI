import uvicorn
from typing import Optional
from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel
import pandas as pd 
import numpy as np
import glob 
#matplotlib
import matplotlib 
import matplotlib.pyplot as plt
#collections
from collections import Counter
#Import paquetes
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution import Colombia, States, Town, Neighborhood



app = FastAPI()
app.include_router(Colombia.router)
app.include_router(States.router)
app.include_router(Town.router)
app.include_router(Neighborhood.router)


#frames = []
#files = glob.glob('assets\*.csv')



@app.get("/")
def main():
    var = "This app is running..."
    return var


# Connection parameters, yours will be different
import psycopg2

param_dic = {
    "host"      : "ec2-54-165-164-38.compute-1.amazonaws.com",
    "database"  : "d42s210pja3o91",
    "user"      : "egxaapodolchzz",
    "password"  : "90f1044690a5e5421eb3d8610ad16c9c7c823201e4e0bf1db96e65dba088184f"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

# Connect to the database
conn = connect(param_dic)
column_names = ["FECHA", "DEPARTAMENTO", "MUNICIPIO", "DIA", "HORA", "BARRIO", "ZONA", "CLASE SITIO", "ARMA EMPLEADA", "EDAD", "SEXO", "ESTADO CIVIL", "CLASE EMPLEADO", "ESCOLARIDAD"]
# Execute the "SELECT *" query
datasetss = postgresql_to_dataframe(conn, "select * from violencia_intrafamiliar_2010", column_names)

#frames.append(addData(files))
#datasets = makeListOfDataFrames(datasets)
#datasets = renameDataFrameColumnsName(datasets)
#datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
#datasets = datasets.dropna()
print(Date(datasetss).byDayName())

