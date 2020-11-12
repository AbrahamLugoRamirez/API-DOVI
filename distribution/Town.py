from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution.Colombia import datasets

router = APIRouter()

@router.get("/bydayname/{departamento}/{municipio}", tags=["Town"])
def chart(departamento: str, municipio:str):
    result = State(datasets, departamento).town(municipio).byDayName()
    return  result

@router.get("/byMonth/{departamento}/{municipio}", tags=["Town"])
def chart(departamento: str, municipio:str):
    result = State(datasets, departamento).town(municipio).byMonth()
    return  result

@router.get("/byWeapon/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getWeapons()
    return result

@router.get("/byWeapon_byDayName/{departamento}/{municipio}/{arma}", tags=["Town"])
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byDayName()    
    return result

@router.get("/byWeapon_byMonth/{departamento}/{municipio}/{arma}", tags=["Town"])
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byMonth()
    return result

@router.get("/bySex/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getSexs()
    return result

@router.get("/bySex_byDayName/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byDayName()
    return result

@router.get("/bySex_byMonth/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byMonth()
    return result

@router.get("/byOld_byDayName/{departamento}/{municipio}/{edad}", tags=["Town"])
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byDayName()
    return result

@router.get("/byOld_byMonth/{departamento}/{municipio}/{edad}", tags=["Town"])
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byMonth()
    return result

@router.get("/bySex_percentage/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    total = State(datasets, departamento).town(municipio).getSex("FEMENINO", values=True) + State(datasets, departamento).town(municipio).getSex("MASCULINO", values=True)
    resultF = (State(datasets, departamento).town(municipio).getSex("FEMENINO", values=True)/total)*100
    resultM = (State(datasets, departamento).town(municipio).getSex("MASCULINO", values=True)/total)*100
    sum = resultF + resultM
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/range/{departamento}/{municipio}", tags=["Town"])
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

@router.get("/byNeighborhood/{departamento}/{municipio}", tags=["State"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).neighborhood().getNeighborhoods()
    return result

@router.get("/Neighborhoods/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).town(municipio).neighborhood().getNeighborhoods()
    return result[0]