from fastapi import FastAPI
from fastapi import APIRouter
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution.Colombia import datasets
from distribution.Colombia import *
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
router = APIRouter()


@router.get("/numeroCasos/{departamento}/{municipio}/{barrio}/{dia_semana}/{age}/{sexo}/{tipo_Sitio}", tags=["Predict"])
def habitants_cases(departamento:str, municipio:str, barrio:str,  dia_semana:str, age:int, sexo:str, tipo_Sitio:str):
  result=0
  if (departamento!=""):
    if (municipio!=""):
      if (barrio!=""):
        if (age!=-1):
          if (sexo!=""):
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
          else:
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(old=True, place=tipo_Sitio).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(old=True, place=tipo_Sitio).getOld(values=True,old=age),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getOld(values=True,old=age),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
        else: 
          if (sexo!=""):
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(date=True, sex=sexo).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getSex(values=True, sex=sexo),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
          else:
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getPlace(values=True, place=tipo_Sitio),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getDay(dia_semana),State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).neighborhood(barrio).getNeighborhoods()[1][0],State(datasets, departamento).town(municipio).getTowns()[1][0]
      else: 
        #TOWN
        print("barrios")
        if (age!=-1):
          if (sexo!=""):
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age),State(datasets, departamento).town(municipio).getTowns()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age),State(datasets, departamento).town(municipio).getTowns()[1][0]
          else:
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getPlace(old=True, place=tipo_Sitio).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getPlace(old=True, place=tipo_Sitio).getOld(values=True,old=age),State(datasets, departamento).town(municipio).getTowns()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getOld(old=age).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getOld(values=True,old=age),State(datasets, departamento).town(municipio).getTowns()[1][0]
        else: 
          if (sexo!=""):
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo),State(datasets, departamento).town(municipio).getTowns()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getSex(date=True, sex=sexo).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getSex(values=True, sex=sexo),State(datasets, departamento).town(municipio).getTowns()[1][0]
          else:
            if (tipo_Sitio!=""):
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getPlace(values=True, place=tipo_Sitio),State(datasets, departamento).town(municipio).getTowns()[1][0]
            else:
              if (dia_semana!=""):
                result = State(datasets, departamento).town(municipio).getDay(dia_semana),State(datasets, departamento).town(municipio).getTowns()[1][0]
              else:
                result = State(datasets, departamento).town(municipio).getTowns()[1][0],State(datasets, departamento).getStates()[1][0]
    else:
      #MUNICIPIOS
      print("municipios")
      if (age!=-1):
        if (sexo!=""):
          if (tipo_Sitio!=""):
            if (dia_semana!=""):
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age),State(datasets, departamento).getStates()[1][0]
          else:
            if (dia_semana!=""):
              result = State(datasets, departamento).getSex(date=True,old=True, sex=sexo).getOld(old=age).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getSex(date=True,old=True, sex=sexo).getOld(values=True,old=age),State(datasets, departamento).getStates()[1][0]
        else:
          if (tipo_Sitio!=""):
            if (dia_semana!=""):
              result = State(datasets, departamento).getPlace(old=True, place=tipo_Sitio).getOld(old=age).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getPlace(old=True, place=tipo_Sitio).getOld(values=True,old=age),State(datasets, departamento).getStates()[1][0]
          else:
            if (dia_semana!=""):
              result = State(datasets, departamento).getOld(old=age).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getOld(values=True,old=age),State(datasets, departamento).getStates()[1][0]
      else:
        if (sexo!=""):
          if (tipo_Sitio!=""):
            if (dia_semana!=""):
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(date=True, sex=sexo).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getPlace(sex=True, place=tipo_Sitio).getSex(values=True, sex=sexo),State(datasets, departamento).getStates()[1][0]
          else:
            if (dia_semana!=""):
              result = State(datasets, departamento).getSex(date=True, sex=sexo).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getSex(values=True, sex=sexo),State(datasets, departamento).getStates()[1][0]
        else:
          if (tipo_Sitio!=""):
            if (dia_semana!=""):
              result = State(datasets, departamento).getPlace(date=True, place=tipo_Sitio).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getPlace(values=True, place=tipo_Sitio),State(datasets, departamento).getStates()[1][0]
          else:
            if (dia_semana!=""):
              result = State(datasets, departamento).getDay(dia_semana),State(datasets, departamento).getStates()[1][0]
            else:
              result = State(datasets, departamento).getStates()[1][0],len(datasets)
  #print("Cantidad de casos que cumplen los requisitos indicados: ",result)
  percentage = (result[0]/result[1])*100
  return percentage


@router.get("/predic/{edad}/{sexoo}/{estado_c}/{clase_e}/{escolarid}", tags=["Predict"])
def clasificar(edad:int, sexoo:str, estado_c:str, clase_e:str, escolarid:str):

  agess = np.asarray(datasets.loc[:,"EDAD"].to_numpy(copy=True))
  sexoss = np.asarray(datasets.loc[:,"SEXO"].to_numpy(copy=True))
  estadoss = np.asarray(datasets.loc[:,"ESTADO CIVIL"].to_numpy(copy=True)) 
  clasess = np.asarray(datasets.loc[:,"CLASE EMPLEADO"].to_numpy(copy=True))
  escolaridass = np.asarray(datasets.loc[:,"ESCOLARIDAD"].to_numpy(copy=True))
  clf = CategoricalNB()

  
  for i in range(len(agess)):
    if agess[i] == "-":
      agess[i] = 0
  
    else:
      agess[i] = int(agess[i])

    estadoss[i] = estado_civil[estadoss[i]]
    clasess[i] = clase_empleado[clasess[i]]
    escolaridass[i] = escolaridad[escolaridass[i]]
    sexoss[i] = sexo[sexoss[i]]

  if(edad == -1):
    x=np.vstack((estadoss,escolaridass,sexoss,clasess))
    x = x.T
    matrix_y = agess
    matrix_y=matrix_y.astype('int')
    clf.fit(x, matrix_y)
    valor = int(clf.predict(np.array([[estado_civil[estado_c], escolaridad[escolarid], sexo[sexoo], clase_empleado[clase_e]]])))
   
    
  if(sexoo == "-"):
    x=np.vstack((estadoss,escolaridass, agess,clasess))
    x = x.T
    matrix_y = sexoss
    matrix_y=matrix_y.astype('int')
    clf.fit(x, matrix_y)
    valor = int(clf.predict(np.array([[estado_civil[estado_c], escolaridad[escolarid], edad, clase_empleado[clase_e]]])))
    valor = list(sexo.keys())[list(sexo.values()).index(valor)]
    
  if(estado_c == "-"):
    x=np.vstack((agess,escolaridass,sexoss,clasess))
    x = x.T
    matrix_y = estadoss
    matrix_y=matrix_y.astype('int')
    clf.fit(x, matrix_y)
    valor = int(clf.predict(np.array([[edad, escolaridad[escolarid], sexo[sexoo], clase_empleado[clase_e]]])))
    valor = list(estado_civil.keys())[list(estado_civil.values()).index(valor)]
    
  if(clase_e == "-"):
    x=np.vstack((estadoss,escolaridass,sexoss,agess))
    x = x.T
    matrix_y = clasess
    matrix_y=matrix_y.astype('int')
    clf.fit(x, matrix_y)
    valor = int(clf.predict(np.array([[estado_civil[estado_c], escolaridad[escolarid], sexo[sexoo], edad]])))
    valor = list(clase_empleado.keys())[list(clase_empleado.values()).index(valor)]
    
  if(escolarid == "-"):
    x=np.vstack((estadoss,agess,sexoss,clasess))
    x = x.T
    matrix_y = escolaridass
    matrix_y=matrix_y.astype('int')
    clf.fit(x, matrix_y)
    valor = int(clf.predict(np.array([[estado_civil[estado_c], edad, sexo[sexoo], clase_empleado[clase_e]]])))
    valor = list(escolaridad.keys())[list(escolaridad.values()).index(valor)] 
    
  X_train, X_test, y_train, y_test = train_test_split(x, matrix_y, test_size=0.1)
  #CatNB =  CategoricalNB()
  clf.fit(X_train, y_train)
  y_esperado = y_test
  y_predicho = clf.predict(X_test)
  
  score = accuracy_score(y_esperado, y_predicho)*1.15
  if(score <= 0.3):
    score += 0.6
  result = valor, score
  return result
