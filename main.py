from fastapi import FastAPI
from dados import Carro

app = FastAPI() # Changed 'site' to 'app' as is common convention for FastAPI instances

@app.get("/Carro")
def get_car_info(): # Changed function name to be more descriptive in English
    return Carro
