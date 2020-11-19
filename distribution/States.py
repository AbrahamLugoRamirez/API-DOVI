from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution.Colombia import datasets
router = APIRouter()


@router.get("/bydayname/{departamento}", tags=["State"])
def chart(departamento: str):
    result = State(datasets, departamento).byDayName()
    return  result

@router.get("/byMonth/{departamento}", tags=["State"])
def chart(departamento: str):
    result = State(datasets, departamento).byMonth()    
    return  result

@router.get("/byWeapon/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).getWeapons()
    return result

@router.get("/byWeapon_byDayName/{departamento}/{arma}", tags=["State"])
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, date=True).byDayName()
    return result

@router.get("/byWeapon_byMonth/{departamento}/{arma}", tags=["State"])
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, date=True).byMonth()
    return result

#Sex
@router.get("/bySex/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).getSexs()
    return result

@router.get("/bySex_byDayName/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = State(datasets, departamento).getSex(sexo, date=True).byDayName()
    return result

@router.get("/bySex_byMonth/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = State(datasets, departamento).getSex(sexo, date=True).byMonth()
    return result

@router.get("/byOld_byDayName/{departamento}/{edad}", tags=["State"])
def chart(departamento:str, edad:str):
    result = State(datasets, departamento).getOld(edad).byDayName()
    return result

@router.get("/byOld_byMonth/{departamento}/{edad}", tags=["State"])
def chart(departamento:str, edad:str):
    result = State(datasets, departamento).getOld(edad).byMonth()
    return result

@router.get("/bySex_percentage/{departamento}", tags=["State"])
def chart(departamento:str):
    total = State(datasets, departamento).getSex("FEMENINO", values=True) + State(datasets, departamento).getSex("MASCULINO", values=True)
    resultF = (State(datasets, departamento).getSex("FEMENINO", values=True)/total)*100
    resultM = (State(datasets, departamento).getSex("MASCULINO", values=True)/total)*100
    sum = resultF + resultM
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/range/{departamento}", tags=["State"])
def chart(departamento:str):
    #por departamento
    result18 = 0
    result45 = 0
    result99 = 0
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


@router.get("/byTown/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).town().getTowns()
    return result

@router.get("/Towns/{departamento}", tags=["State"])
def chart(departamento:str):
    result = State(datasets, departamento).town().getTowns()
    return result[0]


@router.get("/bySex_byWeapon/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = Weapon(State(datasets, departamento).getSex(sexo)).getWeapons()
    return result

@router.get("/bySex_byScholarship/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = Scholarship(State(datasets, departamento).getSex(sexo)).getScholarships()
    return result

@router.get("/bySex_byCivil/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = Civil(State(datasets, departamento).getSex(sexo)).getCivils()
    return result

@router.get("/bySex_byEmployee/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result = Employee(State(datasets, departamento).getSex(sexo)).getEmployees()
    return result

@router.get("/bySex_byAge/{departamento}/{sexo}", tags=["State"])
def chart(departamento:str, sexo:str):
    result= Old(State(datasets, departamento).getSex(sexo)).getOlds()
    return result

@router.get("/byScholarship_byDayName/{departamento}/{escolaridad}", tags=["State"])
def chart(departamento:str, escolaridad:str):
    result = State(datasets, departamento).getScholarship(escolaridad,date=True).byDayName()
    return result

@router.get("/byScholarship_byMonth/{departamento}/{escolaridad}", tags=["State"])
def chart(departamento:str, escolaridad:str):
    result = State(datasets, departamento).getScholarship(escolaridad,date=True).byMonth()
    return result

@router.get("/byScholarship_byWeapon/{departamento}/{escolaridad}", tags=["State"])
def chart(departamento:str, escolaridad:str):
    result = State(datasets, departamento).getScholarship(escolaridad, weapon=True).getWeapons()
    return result

@router.get("/byCivil_byDayName/{departamento}/{civil}", tags=["State"])
def chart(departamento:str, civil:str):
    result = State(datasets, departamento).getCivil(civil,date=True).byDayName()
    return result

@router.get("/byCivil_byMonth/{departamento}/{civil}", tags=["State"])
def chart(departamento:str, civil:str):
    result = State(datasets, departamento).getCivil(civil,date=True).byMonth()
    return result

@router.get("/byCivil_byWeapon/{departamento}/{civil}", tags=["State"])
def chart(departamento:str, civil:str):
    result = State(datasets, departamento).getCivil(civil, weapon=True).getWeapons()
    return result

@router.get("/byWeapon_bySex/{departamento}/{arma}", tags=["State"])
def chart(departamento:str, arma:str):
    result = State(datasets, departamento).getWeapon(arma, sex=True).getSexs()
    return result

@router.get("/byEmployee_byDayName/{departamento}/{empleado}", tags=["State"])
def chart(departamento:str, empleado:str):
    result = State(datasets, departamento).getEmployee(empleado, date=True).byDayName()
    return result

@router.get("/byEmployee_byMonth/{departamento}/{empleado}", tags=["State"])
def chart(departamento:str, empleado:str):
    result = State(datasets, departamento).getEmployee(empleado, date=True).byMonth()
    return result

@router.get("/byEmployee_byWeapon/{departamento}/{empleado}", tags=["State"])
def chart(departamento:str, empleado:str):
    result = State(datasets, departamento).getEmployee(empleado,  weapon=True).getWeapons()
    return result

