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
from models.sort import *


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

frames = []
files = glob.glob('assets\*.csv')
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()

@app.get("/chart_cases_bydaynameColombia")
def chart():
    result = Date(datasets).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@app.get("/chart_cases_byMonthColombia")
def chart():
    result = Date(datasets).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@app.get("/chart_cases_byWeaponColombia")
def chart():
    result = Weapon(datasets).getWeapons()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@app.get("/chart_cases_bySexColombia")
def chart():
    result = Sex(datasets).getSexs()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@app.get("/chart_cases_byStateColombia")
def chart():
    result = State(datasets).getStates()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result


@app.get("/chart_cases_bydayname/{departamento}")
def chart(departamento: str):
    sort = Sort()
    #sex = Sex(datasets)
    result = State(datasets, departamento).byDayName()
    #.town("BARRANQUILLA").neighborhood("VILLA COUNTRY").byDayName()
    dias, cantidad = result
    dias, cantidad = sort.sortValuesAndAdjustNames(dias, cantidad)
    print(dias)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result

@app.get("/chart_cases_bydayname/{departamento}/{municipio}")
def chart(departamento: str, municipio:str):
    sort = Sort()
    sex = Sex(datasets)
    result = State(datasets, departamento).town(municipio).byDayName()
    #.neighborhood("VILLA COUNTRY").byDayName()
    dias, cantidad = result
    dias, cantidad = sort.sortValuesAndAdjustNames(dias, cantidad)
    print(dias)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result

@app.get("/chart_cases_bydayname/{departamento}/{municipio}/{barrio}")
def chart(departamento: str, municipio:str, barrio:str):
    sort = Sort()
    sex = Sex(datasets)
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).byDayName()
    dias, cantidad = result
    dias, cantidad = sort.sortValuesAndAdjustNames(dias, cantidad)
    print(dias)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result


@app.get("/chart_cases_byMonth/{departamento}")
def chart(departamento: str):
    sort = Sort()
    #sex = Sex(datasets)
    result = State(datasets, departamento).byMonth()
    #.town("BARRANQUILLA").neighborhood("VILLA COUNTRY").byDayName()
    dias, cantidad = result
    dias, cantidad = sort.sortValuesAndAdjustNames(dias, cantidad)
    print(dias)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result

@app.get("/chart_cases_byMonth/{departamento}/{municipio}")
def chart(departamento: str, municipio:str):
    sort = Sort()
    sex = Sex(datasets)
    result = State(datasets, departamento).town(municipio).byMonth()
    #.neighborhood("VILLA COUNTRY").byDayName()
    dias, cantidad = result
   # dias, cantidad = sort.sortValuesAndAdjustNames(dias, cantidad)
    print(dias)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result

@app.get("/chart_cases_byMonth/{departamento}/{municipio}/{barrio}")
def chart(departamento: str, municipio:str, barrio:str):
    sort = Sort()
    sex = Sex(datasets)
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).byMonth()
    dias, cantidad = result
   # dias, cantidad = sort.sortValuesAndAdjustNames(dias, cantidad)
    print(dias)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  result


@app.get("/chart_cases_byWeapon/{departamento}")
def chart(departamento:str):
    result = State(datasets, departamento).getWeapons()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_cases_byWeapon/{departamento}/{municipio}")
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getWeapons()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_cases_byWeapon/{departamento}/{municipio}/{barrio}")
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapons()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_byWeapon/{departamento}/{arma}")
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_byWeapon/{departamento}/{municipio}/{arma}")
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_byWeapon/{departamento}/{municipio}/{barrio}/{arma}")
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result


@app.get("/chart_casesbyMonth_byWeapon/{departamento}/{arma}")
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_byWeapon/{departamento}/{municipio}/{arma}")
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_byWeapon/{departamento}/{municipio}/{barrio}/{arma}")
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result



#Sex


@app.get("/chart_cases_bySex/{departamento}")
def chart(departamento:str):
    result = State(datasets, departamento).getSexs()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_cases_bySex/{departamento}/{municipio}")
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getSexs()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_cases_bySex/{departamento}/{municipio}/{barrio}")
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSexs()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_bySex/{departamento}/{sexo}")
def chart(departamento:str, sexo:str):
    result = State(datasets, departamento).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_bySex/{departamento}/{municipio}/{sexo}")
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_bySex/{departamento}/{municipio}/{barrio}/{sexo}")
def chart(departamento:str, municipio:str, barrio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result


@app.get("/chart_casesbyMonth_bySex/{departamento}/{sexo}")
def chart(departamento:str, sexo:str):
    result = State(datasets, departamento).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_bySex/{departamento}/{municipio}/{sexo}")
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_bySex/{departamento}/{municipio}/{barrio}/{sexo}")
def chart(departamento:str, municipio:str, barrio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result


@app.get("/")
def readDataset():
    print("----") 
    print(datasets)
    return {"Hello": "World"}


#print("This is out defff")



