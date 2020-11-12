from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *


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
frames.append(postgresql_to_dataframe(conn, "select * from violencia_intrafamiliar_2019", column_names))
datasets = renameDataFrameColumnsName(frames)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()
conn.close()


@router.get("/bydayname", tags=["Colombia"])
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
    result18 = (result18/sum)*100
    result45 = (result45/sum)*100
    result99 = (result99/sum)*100
    sum3 = result18 + result45 + result99
    result = [["0-18", "19-45", "45 Y MAS"], [result18, result45, result99]]
    return result

@router.get("/numeroCasos/{departamento}/{municipio}/{barrio}/{dia_semana}/{age}/{sexo}/{tipo_Sitio}", tags=["Colombia"])
def habitants_cases(departamento:str, municipio:str, barrio:str,  dia_semana:str, age:int, sexo:str, tipo_Sitio:str):
  result=0
  if (departamento!="-"):
    if (municipio!="-"):
      if (barrio!="-"):
        if (age!=-1):
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
            else:
              result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
          else:
            result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(values=True,old=age)
        else: 
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo)
            else:
              result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(values=True, sex=sexo)
          else:
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(values=True, place=tipo_Sitio)
            else:
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getDay(dia_semana)
              else:
                algo = State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()
                result = algo[1][0]

      else: 
        if (age!=-1):
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
            else:
              result = State(datasets, departamento).town(municipio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
          else:
            result = State(datasets, departamento).town(municipio).getOld(values=True,old=age)
        else: 
          if (sexo!="-"):
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo)
            else:
              result = State(datasets, departamento).town(municipio).getSex(values=True, sex=sexo)
          else:
            if (tipo_Sitio!="-"):
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana)
              else:
                result = State(datasets, departamento).town(municipio).getPlace(values=True, place=tipo_Sitio)
            else:
              if (dia_semana!="-"):
                result = State(datasets, departamento).town(municipio).getDay(dia_semana)
              else:
                algo = State(datasets, departamento).town(municipio).getTowns()
                result = algo[1][0]

    else:
      if (age!=-1):
        if (sexo!="-"):
          if (tipo_Sitio!="-"):
            if (dia_semana!="-"):
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
          else:
            result = State(datasets, departamento).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age)
        else:
          result = State(datasets, departamento).getOld(values=True,old=age)
      else: 
        if (sexo!="-"):
          if (tipo_Sitio!="-"):
            if (dia_semana!="-"):
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo)
          else:
            result = State(datasets, departamento).getSex(values=True, sex=sexo)
        else:
          if (tipo_Sitio!="-"):
            if (dia_semana!="-"):
              result = State(datasets, departamento).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getPlace(values=True, place=tipo_Sitio)
          else:
            if (dia_semana!="-"):
              result = State(datasets, departamento).getDay(dia_semana)
            else:
              result = State(datasets, departamento).getStatess(departamento)
  #print("Cantidad de casos que cumplen los requisitos indicados: ",result)
  return result

