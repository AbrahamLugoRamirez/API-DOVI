
import pandas as pd 
import numpy as np
import glob 

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
