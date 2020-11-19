from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
#from models.places import *

router = APIRouter()
import psycopg2

param_dic = {
    "host"      : "dbapidovi.postgres.database.azure.com",
    "database"  : "violencia_intrafamiliar",
    "user"      : "superuserDOVI@dbapidovi",
    "password"  : "Admindovi123"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

# Connect to the database
conn = connect(param_dic)
column_names = ["FECHA", "DEPARTAMENTO", "MUNICIPIO", "DIA", "HORA", "BARRIO", "ZONA", "CLASE SITIO", "ARMA EMPLEADA", "EDAD", "SEXO", "ESTADO CIVIL", "CLASE EMPLEADO", "ESCOLARIDAD"]
# Execute the "SELECT *" query
# Connect to the database
frames = []
frames.append(postgresql_to_dataframe(conn, "select * from violencia_intrafamiliar_general", column_names))
datasets = renameDataFrameColumnsName(frames)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()
conn.close()


def oldCalculateRange(i,j, lista):
  if (i<=j):
    lista.append(OldRange(datasets).getOld(i,j, iteration=True))
    #print(lista)
    return oldCalculateRange(i+1,j,lista)
  else:
    return lista

class OldRange(Date):   
  def __init__(self, dataset):
    self.dataset = dataset.copy()
    Date.__init__(self, self.dataset.copy())
  def getOld(self, olds,olde,salida=False,iteration=False, values=False):
    result = self.dataset.loc[self.dataset['EDAD'] == olds]
    lista= []
    if values:
      return len(result)
    elif iteration: return result
    elif salida: return joinDataFrames(oldCalculateRange(olds, olde, lista))
    else:
      return Date(result)


@router.get("/byDayName", tags=["Colombia"])
def chart():
    result = Date(datasets).byDayName()
    return result


@router.get("/byMonth", tags=["Colombia"])
def chart():
    result = Date(datasets).byMonth()
    return result

@router.get("/byWeapon", tags=["Colombia"])
def chart():
    result = Weapon(datasets).getWeapons()
    return result

@router.get("/bySex", tags=["Colombia"])
def chart():
    result = Sex(datasets).getSexs()
    return result

@router.get("/bySex_percentage", tags=["Colombia"])
def chart():
    total = Sex(datasets).getSex("MASCULINO", values=True) + Sex(datasets).getSex("FEMENINO", values=True)
    resultM = (Sex(datasets).getSex("MASCULINO", values=True)/total)*100
    resultF = (Sex(datasets).getSex("FEMENINO", values=True)/total)*100
    result = [["FEMENINO", "MASCULINO"], [resultF, resultM]]
    return result

@router.get("/byState", tags=["Colombia"])
def chart():
    result = State(datasets).getStates()
    test_sorting = Sort()
    state, quantity = result
    state, quantity = test_sorting.sortValuesAndAdjustNames(state, quantity)
    return result

@router.get("/range", tags=["Colombia"])
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
    if(sum<=0):
        sum = 1
    result18 = (result18/sum)*100
    result45 = (result45/sum)*100
    result99 = (result99/sum)*100
    sum3 = result18 + result45 + result99
    result = [["0-18", "19-45", "45 Y MAS"], [result18, result45, result99]]
    return result



@router.get("/bySex_byWeapon/{sexo}", tags=["Colombia"])
def chart(sexo:str):
    result = Weapon(Sex(datasets).getSex(sexo)).getWeapons()
    return result

@router.get("/bySex_byScholarship/{sexo}", tags=["Colombia"])
def chart(sexo:str):
    result = Scholarship(Sex(datasets).getSex(sexo)).getScholarships()
    return result

@router.get("/bySex_byCivil/{sexo}", tags=["Colombia"])
def chart(sexo:str):
    result = Civil(Sex(datasets).getSex(sexo)).getCivils()
    return result

@router.get("/bySex_byEmployee/{sexo}", tags=["Colombia"])
def chart(sexo:str):
    result = Employee(Sex(datasets).getSex(sexo)).getEmployees()
    return result

@router.get("/bySex_byAge/{sexo}", tags=["Colombia"])
def chart(sexo:str):
    result= Old(Sex(datasets).getSex(sexo)).getOlds()
    return result

@router.get("/byScholarship_byDayName/{escolaridad}", tags=["Colombia"])
def chart(escolaridad:str):
    result = Scholarship(datasets).getScholarship(escolaridad,date=True).byDayName()
    return result

@router.get("/byScholarship_byMonth/{escolaridad}", tags=["Colombia"])
def chart(escolaridad:str):
    result = Scholarship(datasets).getScholarship(escolaridad,date=True).byMonth()
    return result

@router.get("/byScholarship_byWeapon/{escolaridad}", tags=["Colombia"])
def chart(escolaridad:str):
    result = Scholarship(datasets).getScholarship(escolaridad,weapon=True).getWeapons()
    return result

@router.get("/byCivil_byDayName/{civil}", tags=["Colombia"])
def chart(civil:str):
    result = Civil(datasets).getCivil(civil,date=True).byDayName()
    return result

@router.get("/byCivil_byMonth/{civil}", tags=["Colombia"])
def chart(civil:str):
    result = Civil(datasets).getCivil(civil,date=True).byMonth()
    return result

@router.get("/byCivil_byWeapon/{civil}", tags=["Colombia"])
def chart(civil:str):
    result = Civil(datasets).getCivil(civil,weapon=True).getWeapons()
    return result

@router.get("/byWeapon_bySex/{arma}", tags=["Colombia"])
def chart(arma:str):
    result = Weapon(datasets).getWeapon(arma, sex=True).getSexs()
    return result

@router.get("/byEmployee_byDayName/{empleado}", tags=["Colombia"])
def chart(empleado:str):
    result = Employee(datasets).getEmployee(empleado, date=True).byDayName()
    return result

@router.get("/byEmployee_byMonth/{empleado}", tags=["Colombia"])
def chart(empleado:str):
    result = Employee(datasets).getEmployee(empleado, date=True).byMonth()
    return result

@router.get("/byEmployee_byWeapon/{empleado}", tags=["Colombia"])
def chart(empleado:str):
    result = Employee(datasets).getEmployee(empleado, weapon=True).getWeapons()
    return result

@router.get("/byAgeRange_byDayName/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Date(OldRange(datasets).getOld(inicio,final,salida=True)).byDayName()
    return result

@router.get("/byAgeRange_byMonth/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Date(OldRange(datasets).getOld(inicio,final,salida=True)).byMonth()
    return result

@router.get("/byAgeRange_byWeapon/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Weapon(OldRange(datasets).getOld(inicio,final,salida=True)).getWeapons()
    return result

@router.get("/byAgeRange_bySex/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Sex(OldRange(datasets).getOld(inicio,final,salida=True)).getSexs()
    return result


@router.get("/byAgeRange_byScholarty/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Scholarship(OldRange(datasets).getOld(inicio,final,salida=True)).getScholarships()
    return result

@router.get("/byAgeRange_byCivil/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Civil(OldRange(datasets).getOld(inicio,final,salida=True)).getCivils()
    return result

@router.get("/byAgeRange_byEmployee/{inicio}/{final}", tags=["State"])
def chart(inicio:int, final:int):
    result = Employee(OldRange(datasets).getOld(inicio,final,salida=True)).getEmployees()
    return result






