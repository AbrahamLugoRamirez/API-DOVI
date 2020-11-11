from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *

router = APIRouter()
frames = []
files = glob.glob('assets\*.csv')
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()


@router.get("/chart_cases_bydayname/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
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

@router.get("/chart_cases_byMonth/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
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

@router.get("/chart_cases_byWeapon/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapons()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_byWeapon/{departamento}/{municipio}/{barrio}/{arma}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_byWeapon/{departamento}/{municipio}/{barrio}/{arma}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_cases_bySex/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSexs()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_bySex/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_bySex/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_byOld/{departamento}/{municipio}/{barrio}/{edad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, edad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(edad).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_byOld/{departamento}/{municipio}/{barrio}/{edad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, edad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_cases_bySex_percentage/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    total = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("FEMENINO", values=True) + State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("MASCULINO", values=True)
    resultF = (State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("FEMENINO", values=True)/total)*100
    resultM = (State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("MASCULINO", values=True)/total)*100
    sum = resultF + resultM
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/chart_cases_range/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result18 = 0
    result45 = 0
    result99 = 0
    for i in range(100):
        if(i<=18):
            result18 += State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(i, values=True)
        if(i>18 and i<=45):
            result45 += State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(i, values=True)
        if(i>45):
            result99 += State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(i, values=True)
    sum = result18 + result45 + result99
    result18 = (result18/sum)*100
    result45 = (result45/sum)*100
    result99 = (result99/sum)*100
    sum3 = result18 + result45 + result99
    result = [["0-18", "19-45", "45 Y MAS"], [result18, result45, result99]]
    return result