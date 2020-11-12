from fastapi import Depends, FastAPI, Header, HTTPException
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
    var = "This DOVI-API is running..."
    return var


