from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution.Colombia import *
router = APIRouter()


@router.get("/byDayName/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento: str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()  
    return  result

@router.get("/byMonth/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento: str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()  
    return  result

@router.get("/byWeapon/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapons()
    return result

@router.get("/byWeapon_byDayName/{departamento}/{municipio}/{barrio}/{arma}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()    
    return result

@router.get("/byWeapon_byMonth/{departamento}/{municipio}/{barrio}/{arma}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/bySex/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSexs()
    return result

@router.get("/bySex_byDayName/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo, date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/bySex_byMonth/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, sexo:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byOld_byDayName/{departamento}/{municipio}/{barrio}/{edad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, edad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(edad).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byOld_byMonth/{departamento}/{municipio}/{barrio}/{edad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, edad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(edad).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/bySex_percentage/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    total = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("FEMENINO", values=True) + State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("MASCULINO", values=True)
    resultF = (State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("FEMENINO", values=True)/total)*100
    resultM = (State(datasets, departamento).town(municipio).neighborhood(barrio).getSex("MASCULINO", values=True)/total)*100
    sum = resultF + resultM
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/range/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
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

@router.get("/bySex_byWeapon/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = Weapon(State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo)).getWeapons()
    return result

@router.get("/bySex_byScholarship/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str,  municipio:str, barrio:str, sexo:str):
    result = Scholarship(State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo)).getScholarships()
    return result

@router.get("/bySex_byCivil/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str,  municipio:str, barrio:str, sexo:str):
    result = Civil(State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo)).getCivils()
    return result

@router.get("/bySex_byEmployee/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str,  municipio:str, barrio:str, sexo:str):
    result = Employee(State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo)).getEmployees()
    return result

@router.get("/bySex_byAge/{departamento}/{municipio}/{barrio}/{sexo}", tags=["Neighborhood"])
def chart(departamento:str,  municipio:str, barrio:str, sexo:str):
    result= Old(State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(sexo)).getOlds()
    return result

@router.get("/byScholarship_byDayName/{departamento}/{municipio}/{barrio}/{escolaridad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getScholarship(escolaridad,date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byScholarship_byMonth/{departamento}/{municipio}/{barrio}/{escolaridad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getScholarship(escolaridad,date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byScholarship_byWeapon/{departamento}/{municipio}/{barrio}/{escolaridad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getScholarship(escolaridad, weapon=True).getWeapons()
    return result

@router.get("/byCivil_byDayName/{departamento}/{municipio}/{barrio}/{civil}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, civil:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getCivil(civil,date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byCivil_byMonth/{departamento}/{municipio}/{barrio}/{civil}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, civil:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getCivil(civil,date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byCivil_byWeapon/{departamento}/{municipio}/{barrio}/{civil}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, civil:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getCivil(civil, weapon=True).getWeapons()
    return result

@router.get("/byWeapon_bySex/{departamento}/{municipio}/{barrio}/{arma}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, arma:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getWeapon(arma, sex=True).getSexs()
    return result

@router.get("/byEmployee_byDayName/{departamento}/{municipio}/{barrio}/{empleado}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getEmployee(empleado, date=True).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byEmployee_byMonth/{departamento}/{municipio}/{barrio}/{empleado}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getEmployee(empleado, date=True).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byEmployee_byWeapon/{departamento}/{municipio}/{barrio}/{empleado}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getEmployee(empleado, weapon=True).getWeapons()
    return result

@router.get("/byAgeRange_byDayName/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).byDayName()
    test_sorting = Sort()
    quantity, state = result
    state, quantity= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist() 
    return result

@router.get("/byAgeRange_byMonth/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).byMonth()
    test_sorting = Sort()
    state, quantity = result
    quantity, state= test_sorting.sortValuesAndAdjustNames(quantity, state) 
    result = state.tolist(), quantity.tolist()
    return result

@router.get("/byAgeRange_byWeapon/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).getWeapons()
    return result

@router.get("/byAgeRange_bySex/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).getSexs()
    return result


@router.get("/byAgeRange_byScholarship/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).getScholarships()
    return result

@router.get("/byAgeRange_byCivil/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).getCivils()
    return result

@router.get("/byAgeRange_byEmployee/{departamento}/{municipio}/{barrio}/{inicio}/{final}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, inicio:int, final:int):
    result = State(OldRange(datasets).getOld(inicio,final,salida=True),departamento).town(municipio).neighborhood(barrio).getEmployees()
    return result

@router.get("/byScholarship_bySex/{departamento}/{municipio}/{barrio}/{escolaridad}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, escolaridad:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getScholarship(escolaridad, sex=True).getSexs()
    return result


@router.get("/byCivil_bySex/{departamento}/{municipio}/{barrio}/{civil}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, civil:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getCivil(civil, sex=True).getSexs()
    return result

@router.get("/byEmployee_bySex/{departamento}/{municipio}/{barrio}/{empleado}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str, empleado:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getEmployee(empleado, sex=True).getSexs()
    return result

@router.get("/byEmployee/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getEmployees()
    return result

@router.get("/byScholarship/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getScholarships()
    return result
@router.get("/byCivil/{departamento}/{municipio}/{barrio}", tags=["Neighborhood"])
def chart(departamento:str, municipio:str, barrio:str):
    result = State(datasets, departamento).town(municipio).neighborhood(barrio).getCivils()
    return result



