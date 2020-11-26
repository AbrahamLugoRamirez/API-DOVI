from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution.Colombia import *

router = APIRouter()

@router.get("/byDayName/{departamento}/{municipio}", tags=["Town"])
def chart(departamento: str, municipio:str):
    result = State(datasets, departamento).town(municipio).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return  result

@router.get("/byMonth/{departamento}/{municipio}", tags=["Town"])
def chart(departamento: str, municipio:str):
    result = State(datasets, departamento).town(municipio).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return  result

@router.get("/byWeapon/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getWeapons()
    return result

@router.get("/byWeapon_byDayName/{departamento}/{municipio}/{arma}", tags=["Town"])
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byDayName()    
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byWeapon_byMonth/{departamento}/{municipio}/{arma}", tags=["Town"])
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/bySex/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getSexs()
    return result

@router.get("/bySex_byDayName/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/bySex_byMonth/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str, municipio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byOld_byDayName/{departamento}/{municipio}/{edad}", tags=["Town"])
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byOld_byMonth/{departamento}/{municipio}/{edad}", tags=["Town"])
def chart(departamento:str, municipio:str, edad:str):
    result = State(datasets, departamento).town(municipio).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
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

@router.get("/byNeighborhood/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).neighborhood().getNeighborhoods()
    return result

@router.get("/Neighborhoods/{departamento}", tags=["Town"])
def chart(departamento:str):
    result = State(datasets, departamento).town(municipio).neighborhood().getNeighborhoods()
    return result[0]

@router.get("/bySex_byWeapon/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str, municipio:str, sexo:str):
    result = Weapon(State(datasets, departamento).town(municipio).getSex(sexo)).getWeapons()
    return result

@router.get("/bySex_byScholarship/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str,  municipio:str, sexo:str):
    result = Scholarship(State(datasets, departamento).town(municipio).getSex(sexo)).getScholarships()
    return result

@router.get("/bySex_byCivil/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str,  municipio:str, sexo:str):
    result = Civil(State(datasets, departamento).town(municipio).getSex(sexo)).getCivils()
    return result

@router.get("/bySex_byEmployee/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str,  municipio:str, sexo:str):
    result = Employee(State(datasets, departamento).town(municipio).getSex(sexo)).getEmployees()
    return result

@router.get("/bySex_byAge/{departamento}/{municipio}/{sexo}", tags=["Town"])
def chart(departamento:str,  municipio:str, sexo:str):
    result= Old(State(datasets, departamento).town(municipio).getSex(sexo)).getOlds()
    return result

@router.get("/byScholarship_byDayName/{departamento}/{municipio}/{escolaridad}", tags=["Town"])
def chart(departamento:str, municipio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).getScholarship(escolaridad,date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byScholarship_byMonth/{departamento}/{municipio}/{escolaridad}", tags=["Town"])
def chart(departamento:str, municipio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).getScholarship(escolaridad,date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byScholarship_byWeapon/{departamento}/{municipio}/{escolaridad}", tags=["Town"])
def chart(departamento:str, municipio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).getScholarship(escolaridad, weapon=True).getWeapons()
    return result

@router.get("/byCivil_byDayName/{departamento}/{municipio}/{civil}", tags=["Town"])
def chart(departamento:str, municipio:str, civil:str):
    result = State(datasets, departamento).town(municipio).getCivil(civil,date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byCivil_byMonth/{departamento}/{municipio}/{civil}", tags=["Town"])
def chart(departamento:str, municipio:str, civil:str):
    result = State(datasets, departamento).town(municipio).getCivil(civil,date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byCivil_byWeapon/{departamento}/{municipio}/{civil}", tags=["Town"])
def chart(departamento:str, municipio:str, civil:str):
    result = State(datasets, departamento).town(municipio).getCivil(civil, weapon=True).getWeapons()
    return result

@router.get("/byWeapon_bySex/{departamento}/{municipio}/{arma}", tags=["Town"])
def chart(departamento:str, municipio:str, arma:str):
    result = State(datasets, departamento).town(municipio).getWeapon(arma, sex=True).getSexs()
    return result

@router.get("/byEmployee_byDayName/{departamento}/{municipio}/{empleado}", tags=["Town"])
def chart(departamento:str, municipio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).getEmployee(empleado, date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byEmployee_byMonth/{departamento}/{municipio}/{empleado}", tags=["Town"])
def chart(departamento:str, municipio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).getEmployee(empleado, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byEmployee_byWeapon/{departamento}/{municipio}/{empleado}", tags=["Town"])
def chart(departamento:str, municipio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).getEmployee(empleado, weapon=True).getWeapons()
    return result

@router.get("/byAgeRange_byDayName/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byAgeRange_byMonth/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byAgeRange_byWeapon/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).getWeapons()
    return result

@router.get("/byAgeRange_bySex/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).getSexs()
    return result

@router.get("/byAgeRange_byScholarship/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).getScholarships()
    return result


@router.get("/byAgeRange_byCivil/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).getCivils()
    return result

@router.get("/byAgeRange_byEmployee/{departamento}/{municipio}/{inicio}/{final}", tags=["Town"])
def chart(departamento:str, municipio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).getEmployees()
    return result

@router.get("/byScholarship_bySex/{departamento}/{municipio}/{escolaridad}", tags=["Town"])
def chart(departamento:str, municipio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).getScholarship(escolaridad, sex=True).getSexs()
    return result

@router.get("/byCivil_bySex/{departamento}/{municipio}/{civil}", tags=["Town"])
def chart(departamento:str, municipio:str, civil:str):
    result = State(datasets, departamento).town(municipio).getCivil(civil, sex=True).getSexs()
    return result

@router.get("/byEmployee_bySex/{departamento}/{municipio}/{empleado}", tags=["Town"])
def chart(departamento:str, municipio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).getEmployee(empleado, sex=True).getSexs()
    return result


@router.get("/byEmployee/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getEmployees()
    return result

@router.get("/byScholarship/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getScholarships()
    return result
@router.get("/byCivil/{departamento}/{municipio}", tags=["Town"])
def chart(departamento:str, municipio:str):
    result = State(datasets, departamento).town(municipio).getCivils()
    return result