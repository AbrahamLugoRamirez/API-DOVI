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


@router.get("/chart_cases_bydayname/{departamento}/{municipio}")
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

@router.get("/chart_cases_byMonth/{departamento}/{municipio}")
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

@router.get("/chart_cases_byWeapon/{departamento}/{municipio}")
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getWeapons()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_byWeapon/{departamento}/{municipio}/{arma}")
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_byWeapon/{departamento}/{municipio}/{arma}")
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_cases_bySex/{departamento}/{municipio}")
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getSexs()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_bySex/{departamento}/{municipio}/{sexo}")
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_cases_bySex/{departamento}/{municipio}/{barrio}")
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSexs()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result


@router.get("/chart_casesbyMonth_bySex/{departamento}/{municipio}/{sexo}")
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_byOld/{departamento}/{municipio}/{edad}")
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_byOld/{departamento}/{municipio}/{edad}")
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_cases_bySex_percentage/{departamento}/{municipio}")
def chart(departamento:str, municipio:str):
    total = State(datasets, departamento).town(municipio).getSex("FEMENINO", values=True) + State(datasets, departamento).town(municipio).getSex("MASCULINO", values=True)
    resultF = (State(datasets, departamento).town(municipio).getSex("FEMENINO", values=True)/total)*100
    resultM = (State(datasets, departamento).town(municipio).getSex("MASCULINO", values=True)/total)*100
    sum = resultF + resultM
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/chart_cases_range/{departamento}/{municipio}")
def chart(departamento:str, municipio:str):
    result18 = 0
    result45 = 0
    result99 = 0
    for i in range(100):
        if(i<=18):
            result18 += State(datasets, departamento).town(municipio).getOld(i, values=True)
        if(i>18 and i<=45):
            result45 += State(datasets, departamento).town(municipio).getOld(i, values=True)
        if(i>45):
            result99 += State(datasets, departamento).town(municipio).getOld(i, values=True)
    sum = result18 + result45 + result99
    result18 = (result18/sum)*100
    result45 = (result45/sum)*100
    result99 = (result99/sum)*100
    sum3 = result18 + result45 + result99
    result = [["0-18", "19-45", "45 Y MAS"], [result18, result45, result99]]
    return result