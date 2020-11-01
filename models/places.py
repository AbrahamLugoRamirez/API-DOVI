from collections import Counter

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

