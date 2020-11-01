from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd 
import numpy as np
import glob 

#matplotlib
import matplotlib 
import matplotlib.pyplot as plt

#collections
from collections import Counter

#Tensorflow - Keras
#import tensorflow as tfj
#from tensorflow.keras import Sequential

#%matplotlib inline
app = FastAPI()
#git clone https://github.com/AbrahamLugoRamirez/Violence_dataset


habitantes_por_departamento = {
    "AMAZONAS": 79739,
    "ANTIOQUIA": 6768388,
    "ARAUCA": 273321,
    "ATLÁNTICO": 2573591,
    "BOLIVAR": 2195495,
    "BOYACA": 1284375,
    "CALDAS": 995822,
    "CAQUETA": 502410,
    "CASANARE": 381554,
    "CAUCA": 1426938,
    "CESAR": 1077770,
    "CHOCO": 520296,
    "CUNDINAMARCA": 2845668,
    "CORDOBA": 1813854,
    "GUAINIA": 44134,
    "GUAJIRA": 1067063,
    "GUAVIARE": 117494,
    "HUILA": 1211163,
    "MAGDALENA": 1312428,
    "META": 1035256,
    "NARIÑO": 1830473,
    "NORTE DE SANTANDER": 1402695,
    "PUTUMAYO": 363597,
    "QUINDIO": 578268,
    "RISARALDA": 972978,
    "SAN ANDRES": 79060,
    "SANTANDER": 2100704,
    "SUCRE": 885835,
    "TOLIMA": 1423715,
    "VALLE": 4804489,
    "VAUPES": 45367,
    "VICHADA": 79134,
} 

habitantes_departamento=[["AMAZONAS",
    "ANTIOQUIA",
    "ARAUCA",
    "ATLÁNTICO",
    "BOLIVAR",
    "BOYACA",
    "CALDAS",
    "CAQUETA",
    "CASANARE",
    "CAUCA",
    "CESAR",
    "CHOCO",
    "CUNDINAMARCA",
    "CORDOBA",
    "GUAINIA",
    "GUAJIRA",
    "GUAVIARE",
    "HUILA",
    "MAGDALENA",
    "META",
    "NARIÑO",
    "NORTE DE SANTANDER",
    "PUTUMAYO",
    "QUINDIO",
    "RISARALDA",
    "SAN ANDRES",
    "SANTANDER",
    "SUCRE",
    "TOLIMA",
    "VALLE",
    "VAUPES",
    "VICHADA"],[79739,
     6768388,
     273321,
     2573591,
     2195495,
     1284375,
     995822,
     502410,
     381554,
     1426938,
     1077770,
     520296,
     2845668,
     1813854,
     44134,
     1067063,
     117494,
     1211163,
     1312428,
     1035256,
     1830473,
     1402695,
     363597,
     578268,
     972978,
     79060,
     2100704,
     885835,
     1423715,
     4804489,
     45367,
     79134]]

#Clase Sort
class Sort:
    
  def sortValues(values):
    values = np.array(values)
    index = np.argsort(values).flatten()
    values = values[index]
    return values
    
  def sortValuesAndAdjustNames(self, names, values):
    names, values = np.array(names), np.array(values)

    index = np.argsort(values).flatten()
    names, values = names[index], values[index]

    return names, values

#class Plot

class Plot:
    
  def __init__(self, y, x, title="title"):
    self.y_label, self.y_value = y
    self.x_label, self.x_value = x
    self.title = title

  def histogram(self, figsize=(32, 40)):
    plt.figure(figsize=figsize)
    plt.barh(self.y_value, self.x_value)
    plt.title(self.title)
    plt.xlabel(self.x_label)
    plt.ylabel(self.y_label)

    # Setting values to each bar
    for index, value in enumerate(self.x_value):
      plt.text(y=index, x=value, s=value)

    plt.show()


#Class date
class Date:
    
  def __init__(self, dataset):
    self.dataset = dataset.copy()
    
  def byYear(self):
    result = [i[6:10] for i in self.dataset["FECHA"]]
    return self.__uniq_values(result)

  def byMonth(self):
    result = [i[:2] for i in self.dataset["FECHA"]]
    return self.__uniq_values(result)

  def byWeek(self):
    return "week"

  def byDay(self):
    result = [i[3:5] for i in self.dataset["FECHA"]]
    return self.__uniq_values(result)

  def byDayName(self):
    result = self.dataset["DIA"]
    return self.__uniq_values(result)

  def getDay(self, day):
    result = self.dataset.loc[self.dataset['DIA'] == day]
    return len(result)
        
  def byHour(self):
    hour_len = 11
    result = [i if len(i) <= hour_len else i[-11:] for i in self.dataset["HORA"]]
    result = ["{}:00:00 {}".format(i[:2], i[-2:]) for i in result]
    return self.__uniq_values(result) 

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    #Name of dates
    dates = list(uniq_dates.keys())
    #get amount of occurrencies per date
    amount = list(uniq_dates.values())

    return dates, amount



#Clas Old

class Old(Date):
   
  def __init__(self, dataset):
    self.dataset = dataset.copy()
    Date.__init__(self, self.dataset.copy())

  def getOld(self, old, values=False):
    result = self.dataset.loc[self.dataset['EDAD'] == old]
    if values:
      return len(result)
    else:
      return Date(result)

  def getOlds(self):
    result = self.dataset["EDAD"]
    return self.__uniq_values(result)

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    #Name of dates
    dates = list(uniq_dates.keys())
    #get amount of occurrencies per date
    amount = list(uniq_dates.values())

    return dates, amount   


#class SexXx

class Sex(Old, Date):
   
  def __init__(self, dataset):
    self.dataset = dataset.copy()
    Date.__init__(self, self.dataset.copy())
    Old.__init__(self, self.dataset.copy())

  def getSex(self, sex, values=False, old=False, date=False):
    result = self.dataset.loc[self.dataset['SEXO'] == sex]
    if values:
      return len(result)
    else:
      if old: return Old(result)
      elif date: return Date(result)
      else: None

  def getSexs(self):
    result = self.dataset["SEXO"]
    return self.__uniq_values(result)

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    #Name of dates
    dates = list(uniq_dates.keys())
    #get amount of occurrencies per date
    amount = list(uniq_dates.values())

    return dates, amount   

#Class Weapon

class Weapon(Sex, Old, Date):

  def __init__(self, dataset):
    self.dataset = dataset.copy()
    Date.__init__(self, self.dataset)
    Sex.__init__(self, self.dataset)
    Old.__init__(self, self.dataset)

  def getWeapon(self, weapon, values=False, date=False, sex=False, old=False):
    result = self.dataset.loc[self.dataset['ARMA EMPLEADA'] == weapon]
    if values:
      return len(result)
    else:
      if sex: return Sex(result)
      elif date: return Date(result)
      elif old: return Old(result)
      else: None

  def getWeapons(self):
    result = self.dataset["ARMA EMPLEADA"]
    return self.__uniq_values(result)

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    # Names 
    names = list(uniq_dates.keys())
    # Get amount of occurrencies 
    amount = list(uniq_dates.values())

    return names, amount



#Clase Place

class Place(Weapon, Sex, Old, Date):

  def __init__(self, dataset):
    self.dataset = dataset.copy()
    Date.__init__(self, self.dataset.copy())
    Weapon.__init__(self, self.dataset.copy())
    Sex.__init__(self, self.dataset.copy())
    Old.__init__(self, self.dataset.copy())

  def getPlace(self, place, values=False, sex=False, date=False, weapon=False, old=False):
    result = self.dataset.loc[self.dataset['CLASE SITIO'] == place]
    if values:
      return len(result)
    else:
      if date: return Date(result)
      elif weapon: return Weapon(result)
      elif sex: return Sex(result)
      elif old: return Old(result)
      else: None

  # Casos de SITIOS DE VIOLENCIA en general
  def getPlaces(self):
    result = self.dataset['CLASE SITIO']
    return self.__uniq_values(result)

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    # Names 
    names = list(uniq_dates.keys())
    # Get amount of occurrencies 
    amount = list(uniq_dates.values())

    return names, amount


#Class Neighborhood

class Neighborhood(Place, Weapon, Sex, Date):
    
  def __init__(self, dataset, neighborhood=".$"):
    self.dataset = dataset
    self.neighborhood = neighborhood
    self.neighborhood_dataset = self.__getNeighborhood(self.neighborhood)
    Date.__init__(self, self.neighborhood_dataset.copy())
    Place.__init__(self, self.neighborhood_dataset.copy())
    Weapon.__init__(self, self.neighborhood_dataset.copy())
    Sex.__init__(self, self.neighborhood_dataset.copy())

  def __getNeighborhood(self, neighborhood):
    return self.dataset.loc[self.dataset['BARRIO'].str.contains(neighborhood)]
    
  def getNeighborhood(self, neighborhood):
    return self.__uniq_values(self.__getNeighborhood(neighborhood))

  def getNeighborhoods(self):
    return self.__uniq_values(self.dataset["BARRIO"])


  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    # Names 
    names = list(uniq_dates.keys())
    # Get amount of occurrencies 
    amount = list(uniq_dates.values())

    return names, amount


#Class Town

class Town(Place, Weapon, Sex,Date):
    
  def __init__(self, dataset, town=".$"):
    self.town = town
    self.dataset = dataset
    self.town_dataset = self.__getTown(self.town)

    # these params are completly necesary.
    # These params are used to plot results
    # items means columns or a set of keys into the dataset
    # value of the foud items
    self.values = []
    #name of the found items
    self.names = []


    Date.__init__(self, self.town_dataset)
    Place.__init__(self, self.town_dataset.copy())
    Weapon.__init__(self, self.town_dataset.copy())
    Sex.__init__(self, self.town_dataset.copy())

  def neighborhood(self, neighborhood=".$"):
    return Neighborhood(self.town_dataset.copy(), neighborhood)

  def __getTown(self, town):
    return self.dataset.loc[self.dataset["MUNICIPIO"].str.contains(town)]

  def getTown(self, town):
    return self.__getTown(town)

  def getTowns(self):
    result = self.dataset["MUNICIPIO"]
    return self.__uniq_values(result)

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    # Names 
    names = list(uniq_dates.keys())
    # Get amount of occurrencies 
    amount = list(uniq_dates.values())

    return names, amount


#Clase State
class State(Place, Weapon, Sex, Date):
    
  def __init__(self, dataset, state='.$'):
    self.state = state
    self.dataset = dataset.copy()
    self.state_dataset = self.__getState(self.state)

    # these params are completly necesary.
    # These params are used to plot results
    # items means columns or a set of keys into the dataset
    # value of the foud items
    self.values = []
    #name of the found itemsAro
    self.names = []

    Date.__init__(self, self.state_dataset)
    Place.__init__(self, self.state_dataset.copy())
    Weapon.__init__(self, self.state_dataset.copy())
    Sex.__init__(self, self.state_dataset.copy())

  def __getState(self, state):
    result = self.dataset.loc[self.dataset['DEPARTAMENTO'].str.contains(state)]
    return result

  def town(self, town=".$"):
    return Town(self.state_dataset.copy(), town)

  def getState(self, state):
    return self.__uniq_values(self.__getState(state))

  def getStates(self):
    result = self.dataset["DEPARTAMENTO"]
    return self.__uniq_values(result)

  def getStatess(self, state):
    result = self.dataset.loc[self.dataset['DEPARTAMENTO'] == state]
    return len(result)

  def __uniq_values(self, dataset):
    #unique dates
    uniq_dates = Counter(dataset)

    # Names 
    names = list(uniq_dates.keys())
    # Get amount of occurrencies 
    amount = list(uniq_dates.values())

    return names, amount






def addData(files: str) -> list:
        allCsv = []
        for file in files:
            temp = open(file, 'r', encoding='utf-8')
            tempDf = pd.read_csv(temp)
            allCsv.append(tempDf)
            
        return allCsv

def renameDataFrameColumnsName(dataframes):
    for i in range(len(dataframes)):
        dataframes[i].columns = dataframes[i].columns.str.upper()
        dataframes[i].columns = dataframes[i].columns.str.lstrip()
        dataframes[i].columns = dataframes[i].columns.str.replace('Á', 'A')
        dataframes[i].columns = dataframes[i].columns.str.replace('É', 'E')
        dataframes[i].columns = dataframes[i].columns.str.replace('Í', 'I')
        dataframes[i].columns = dataframes[i].columns.str.replace('Ó', 'O')
        dataframes[i].columns = dataframes[i].columns.str.replace('Ú', 'U')
        dataframes[i].columns = dataframes[i].columns.str.replace(' DE ', ' ')
    return dataframes
    
def makeListOfDataFrames(list_of_dataframes):
    auxiliar_list = []
    len_of_dataframes = len(list_of_dataframes[0])
    for i in range(len_of_dataframes):
        dt = pd.DataFrame(list_of_dataframes[0][i])
        auxiliar_list.append(dt)
    return auxiliar_list

def joinDataFrames(dataframes):
    return pd.concat(dataframes)


frames = []
    #file1 = np.genfromtxt('path/to/myfile.csv',delimiter=',',skiprows=1)

    #Create a list ('frames') with four nested lists, one per sensor. 
    #Each nested list have all the samples (DF) for that sensor.
    #%cd /Violence_dataset
files = glob.glob('assets\*.csv')
    #files = pd.read_csv('Violencia_intrafamiliar_2010.csv')
    #files.sort()
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
    ## Delete all rows which has some NAN value
datasets = datasets.dropna()
#print(datasets)


@app.get("/histogram/{departamento}")
def histogram(departamento: str):
    sort = Sort()
    sex = Sex(datasets)
    result = State(datasets, departamento).town("BARRANQUILLA").neighborhood("VILLA COUNTRY").byDayName()
    sexo, cantidad = result
    sexo, cantidad = sort.sortValuesAndAdjustNames(sexo, cantidad)
    print(sexo)
    print(cantidad)
    #plot = Plot(("sexo", sexo), ("cantidad", cantidad), title="Dias complicados en el barrio Villa Country, Barranquilla - Atlantico, para el genero femenino")
    #plot.histogram(figsize=(32, 14))
    return  {"Histogram": "Great"}



@app.get("/")
def readDataset():
    print("----") 
    print(datasets)
    return {"Hello": "World"}


#print("This is out defff")



