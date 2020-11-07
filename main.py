import uvicorn
from typing import Optional
from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel
import pandas as pd 
import numpy as np
import glob 
#matplotlib
import matplotlib 
import matplotlib.pyplot as plt
#collections
from collections import Counter
#Import paquetes
from configurations.functions import *
from models.places import *
from models.sort import *
from models.dictionaries import *
from distribution import Colombia, States, Town, Neighborhood

from app.router import api_router

#app = FastAPI()
app = FastAPI(docs_url=None,redoc_url=None)
app.include_router(api_router, prefix="/v1")
app.include_router(Colombia.router)
app.include_router(States.router)
app.include_router(Town.router)
app.include_router(Neighborhood.router)


frames = []
files = glob.glob('assets\*.csv')
frames.append(addData(files))
datasets = makeListOfDataFrames(frames)
datasets = renameDataFrameColumnsName(datasets)
datasets = joinDataFrames(datasets)
## Delete all rows which has some NAN value
datasets = datasets.dropna()


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')

@app.get("/")
def main():
    var = "This app is running..."
    return var


