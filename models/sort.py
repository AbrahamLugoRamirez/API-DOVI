import numpy as np
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
