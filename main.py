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

#git clone https://github.com/AbrahamLugoRamirez/Violence_dataset

frames = []
files = glob.glob('assets\*.csv')
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()

@app.get("/")
def main():
    var = "This app is running"
    return var

@app.get("/numeroCasos/{departamento}/{municipio}/{barrio}/{dia_semana}/{age}/{sexo}/{tipo_Sitio}")
def habitants_cases(departamento , municipio, barrio,  dia_semana, age, sexo, tipo_Sitio):
  result=0
  if (departamento!="-"):
    if (municipio!="-"):
      if (barrio!="-"):
        if (age!=-1):
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
            else:
              result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
          else:
            result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(values=True,old=age)
        else: 
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo)
            else:
              result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(values=True, sex=sexo)
          else:
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(values=True, place=tipo_Sitio)
            else:
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getDay(dia_semana)
              else:
                algo = State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()
                result = algo[1][0]

      else: 
        if (age!=-1):
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
            else:
              result = State(datasets, departamento).town(municipio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
          else:
            result = State(datasets, departamento).town(municipio).getOld(values=True,old=age)
        else: 
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo)
            else:
              result = State(datasets, departamento).town(municipio).getSex(values=True, sex=sexo)
          else:
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).getPlace(values=True, place=tipo_Sitio)
            else:
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getDay(dia_semana)
              else:
                algo = State(datasets, departamento).town(municipio).getTowns()
                result = algo[1][0]

    else:
      if (age!=-1):
        if (sexo!="-"):
          if (tipo_Sitio!="-"):
            if (dia_semana!="-"):
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
          else:
            result = State(datasets, departamento).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
        else:
          result = State(datasets, departamento).getOld(values=True,old=age)
      else: 
        if (sexo!="-"):
          if (tipo_Sitio!="-"):
            if (dia_semana!="-"):
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo)
          else:
            result = State(datasets, departamento).getSex(values=True, sex=sexo)
        else:
          if (tipo_Sitio!="-"):
            if (dia_semana!="-"):
              result = State(datasets, departamento).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getPlace(values=True, place=tipo_Sitio)
          else:
            if (dia_semana!="-"):
              result = State(datasets, departamento).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getStatess(departamento)
  print("Cantidad de casos que cumplen los requisitos indicados: ",result)
  return result



