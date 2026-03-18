from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def mensaje():
    return "Bienvenidos a FastAPI Ingenieros de Sistemas y computación"

@app.get('/{nombre}/{codigo}')
def mensaje2(nombre:str,codigo:int):
    return f"Bienvenido {nombre}, su codigo es: {codigo}"

@app.get('/uno/')
def mensaje3(edad:int):
    return f"su edad es {edad}"

@app.get('/dos/')
def mensaje3(nombre:str,edad:int):
    return f"hola {nombre}, su edad es: {edad}"