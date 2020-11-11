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


@router.get("/chart_cases_bydayname/{departamento}", tags=["State"])
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

@router.get("/chart_cases_byMonth/{departamento}", tags=["State"])
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

@router.get("/chart_cases_byWeapon/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).getWeapons()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_byWeapon/{departamento}/{arma}", tags=["State"])
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_byWeapon/{departamento}/{arma}", tags=["State"])
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

#Sex
@router.get("/chart_cases_bySex/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).getSexs()
    print(result)
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_bySex/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = State(datasets, departamento).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_bySex/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = State(datasets, departamento).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyDayName_byOld/{departamento}/{edad}", tags=["State"])
def chart(departamento:str, edad:str):
    result = State(datasets, departamento).getOld(edad).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_casesbyMonth_byOld/{departamento}/{edad}", tags=["State"])
def chart(departamento:str, edad:str):
    result = State(datasets, departamento).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    #testing_plot = Plot(("Weapon", state), ("quantity", quantity), title="states")
    #testing_plot.histogram()
    return result

@router.get("/chart_cases_bySex_percentage/{departamento}", tags=["State"])
def chart(departamento:str):
    total = State(datasets, departamento).getSex("FEMENINO", values=True) + State(datasets, departamento).getSex("MASCULINO", values=True)
    resultF = (State(datasets, departamento).getSex("FEMENINO", values=True)/total)*100
    resultM = (State(datasets, departamento).getSex("MASCULINO", values=True)/total)*100
    sum = resultF + resultM
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/chart_cases_range/{departamento}", tags=["State"])
def chart(departamento:str):
    #por departamento
    result18 = 0
    result45 = 0
    result99 = 0
#print(Old(datasets).getOld(1, values=True))
    for i in range(100):
        if(i<=18):
            result18 += State(datasets, departamento).getOld(i, values=True)
        if(i>18 and i<=45):
            result45 += State(datasets, departamento).getOld(i, values=True)
        if(i>45):
            result99 += State(datasets, departamento).getOld(i, values=True)
    sum = result18 + result45 + result99
    result18 = (result18/sum)*100
    result45 = (result45/sum)*100
    result99 = (result99/sum)*100
    sum3 = result18 + result45 + result99
    result = [["0-18", "19-45", "45 Y MAS"], [result18, result45, result99]]
    return result