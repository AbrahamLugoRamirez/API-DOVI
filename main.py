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
from models.dictionaries import *

app = FastAPI()
#git clone https://github.com/AbrahamLugoRamirez/Violence_dataset

frames = []
files = glob.glob('assets\*.csv')
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()


#Global Get-- Colombia
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

@app.get("/chart_cases_bySexColombia_Porcentaje")
def chart():
    resultM = (Sex(datasets).getSex("MASCULINO", values=True)/346279)*100
    resultF = (Sex(datasets).getSex("FEMENINO", values=True)/346279)*100
    resultNo = ((346279 - (Sex(datasets).getSex("FEMENINO", values=True)+Sex(datasets).getSex("MASCULINO", values=True)))/346279)*100
    sum = resultF + resultM + resultNo
    result = [["MASCULINO", "FEMENINO", "NO REPORTADO"], [resultM, resultF, resultNo]]
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


#Edad
@app.get("/chart_casesbyDayName_byOld/{departamento}/{edad}")
def chart(departamento:str, edad:str):
    result = State(datasets, departamento).getOld(edad).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_byOld/{departamento}/{municipio}/{edad}")
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyDayName_byOld/{departamento}/{municipio}/{barrio}/{edad}")
def chart(departamento:str, municipio:str, barrio:str, edad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(edad).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_byOld/{departamento}/{edad}")
def chart(departamento:str, edad:str):
    result = State(datasets, departamento).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_byOld/{departamento}/{municipio}/{edad}")
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@app.get("/chart_casesbyMonth_byOld/{departamento}/{municipio}/{barrio}/{edad}")
def chart(departamento:str, municipio:str, barrio:str, edad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result


@app.get("/")
def readDataset():
    #print(datasets)
    var = "This app is running"
    return var


#print("This is out defff")



