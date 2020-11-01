from typing import Optional

from fastapi import FastAPI
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

app = FastAPI()
#git clone https://github.com/AbrahamLugoRamirez/Violence_dataset


habitantes_por_departamento = {
    "AMAZONAS": 79739,
    "ANTIOQUIA": 6768388,
    "ARAUCA": 273321,
    "ATLÁNTICO": 2573591,
    "BOLIVAR": 2195495,
    "BOYACA": 1284375,
    "CALDAS": 995822,
    "CAQUETA": 502410,
    "CASANARE": 381554,
    "CAUCA": 1426938,
    "CESAR": 1077770,
    "CHOCO": 520296,
    "CUNDINAMARCA": 2845668,
    "CORDOBA": 1813854,
    "GUAINIA": 44134,
    "GUAJIRA": 1067063,
    "GUAVIARE": 117494,
    "HUILA": 1211163,
    "MAGDALENA": 1312428,
    "META": 1035256,
    "NARIÑO": 1830473,
    "NORTE DE SANTANDER": 1402695,
    "PUTUMAYO": 363597,
    "QUINDIO": 578268,
    "RISARALDA": 972978,
    "SAN ANDRES": 79060,
    "SANTANDER": 2100704,
    "SUCRE": 885835,
    "TOLIMA": 1423715,
    "VALLE": 4804489,
    "VAUPES": 45367,
    "VICHADA": 79134,
} 

habitantes_departamento=[["AMAZONAS",
    "ANTIOQUIA",
    "ARAUCA",
    "ATLÁNTICO",
    "BOLIVAR",
    "BOYACA",
    "CALDAS",
    "CAQUETA",
    "CASANARE",
    "CAUCA",
    "CESAR",
    "CHOCO",
    "CUNDINAMARCA",
    "CORDOBA",
    "GUAINIA",
    "GUAJIRA",
    "GUAVIARE",
    "HUILA",
    "MAGDALENA",
    "META",
    "NARIÑO",
    "NORTE DE SANTANDER",
    "PUTUMAYO",
    "QUINDIO",
    "RISARALDA",
    "SAN ANDRES",
    "SANTANDER",
    "SUCRE",
    "TOLIMA",
    "VALLE",
    "VAUPES",
    "VICHADA"],[79739,
     6768388,
     273321,
     2573591,
     2195495,
     1284375,
     995822,
     502410,
     381554,
     1426938,
     1077770,
     520296,
     2845668,
     1813854,
     44134,
     1067063,
     117494,
     1211163,
     1312428,
     1035256,
     1830473,
     1402695,
     363597,
     578268,
     972978,
     79060,
     2100704,
     885835,
     1423715,
     4804489,
     45367,
     79134]]

#Clase Sort
class Sort:
    
  def sortValues(values):
    values = np.array(values)
    index = np.argsort(values).flatten()
    values = values[index]
    return values
    
  def sortValuesAndAdjustNames(self, names, values):
    names, values = np.array(names), np.array(values)

    index = np.argsort(values).flatten()
    names, values = names[index], values[index]

    return names, values

#class Plot

class Plot:
    
  def __init__(self, y, x, title="title"):
    self.y_label, self.y_value = y
    self.x_label, self.x_value = x
    self.title = title

  def histogram(self, figsize=(32, 40)):
    plt.figure(figsize=figsize)
    plt.barh(self.y_value, self.x_value)
    plt.title(self.title)
    plt.xlabel(self.x_label)
    plt.ylabel(self.y_label)

    # Setting values to each bar
    for index, value in enumerate(self.x_value):
      plt.text(y=index, x=value, s=value)

    plt.show()


#Class date





frames = []
    #file1 = np.genfromtxt('path/to/myfile.csv',delimiter=',',skiprows=1)

    #Create a list ('frames') with four nested lists, one per sensor. 
    #Each nested list have all the samples (DF) for that sensor.
    #%cd /Violence_dataset
files = glob.glob('assets\*.csv')
    #files = pd.read_csv('Violencia_intrafamiliar_2010.csv')
    #files.sort()
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
    ## Delete all rows which has some NAN value
datasets = datasets.dropna()
#print(datasets)


@app.get("/histogram/{departamento}")
def histogram(departamento: str):
    sort = Sort()
    sex = Sex(datasets)
    result = State(datasets, departamento).byDayName()
    #.town("BARRANQUILLA").neighborhood("VILLA COUNTRY").byDayName()
    sexo, cantidad = result
    sexo, cantidad = sort.sortValuesAndAdjustNames(sexo, cantidad)

    print(sexo)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result



@app.get("/")
def readDataset():
    print("----") 
    print(datasets)
    return {"Hello": "World"}


#print("This is out defff")



