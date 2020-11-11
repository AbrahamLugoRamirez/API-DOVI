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
from distribution import *
from distribution import Neigh
from distribution import Colombia, States, Town
from distribution.Colombia import datasets


app = FastAPI()
app.include_router(Colombia.router)
app.include_router(States.router)
app.include_router(Neigh.router)
app.include_router(Town.router)







@app.get("/")
def main():
    var = "This app is running..."
    return var


