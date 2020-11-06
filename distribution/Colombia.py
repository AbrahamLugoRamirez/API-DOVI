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


@router.get("/chart_cases_bydayname", tags=["Colombia"])
def chart():
    result = Date(datasets).byDayName()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result


@router.get("/chart_cases_byMonth", tags=["Colombia"])
def chart():
    result = Date(datasets).byMonth()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@router.get("/chart_cases_byWeapon", tags=["Colombia"])
def chart():
    result = Weapon(datasets).getWeapons()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@router.get("/chart_cases_bySex", tags=["Colombia"])
def chart():
    result = Sex(datasets).getSexs()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@router.get("/chart_cases_bySex_percentage", tags=["Colombia"])
def chart():
    total = Sex(datasets).getSex("MASCULINO", values=True) + Sex(datasets).getSex("FEMENINO", values=True)
    resultM = (Sex(datasets).getSex("MASCULINO", values=True)/total)*100
    resultF = (Sex(datasets).getSex("FEMENINO", values=True)/total)*100
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/chart_cases_byState", tags=["Colombia"])
def chart():
    result = State(datasets).getStates()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@router.get("/chart_cases_range", tags=["Colombia"])
def chart():
    result18 = 0
    result45 = 0
    result99 = 0
    for i in range(100):
        if(i<=18):
            result18 += Old(datasets).getOld(i, values=True)
        if(i>18 and i<=45):
            result45 +=Old(datasets).getOld(i, values=True)
        if(i>45):
            result99 += Old(datasets).getOld(i, values=True)
    sum = result18 + result45 + result99
    result18 = (result18/sum)*100
    result45 = (result45/sum)*100
    result99 = (result99/sum)*100
    sum3 = result18 + result45 + result99
    result = [["0-18", "19-45", "45 Y MAS"], [result18, result45, result99]]
    return result