from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
import json
import os

app=FastAPI()

# Cargar productos desde el archivo JSON al iniciar la aplicación
archivo_json = "productos.json"

# Función para cargar productos desde JSON
def cargar_productos():
    lista = []
    if os.path.exists(archivo_json):
        with open(archivo_json, mode='r', encoding='utf-8') as file:
            lista = json.load(file)
    return lista

# Lista de productos en memoria
def guardar_productos():
    with open(archivo_json, mode='w', encoding='utf-8') as file:
        json.dump(productos, file, indent=4)

# Cargar productos al iniciar la aplicación
productos = cargar_productos()

@app.get('/')
def mensaje():
    return "Bienvenidos a FastAPI Ingenieros de Sistemas y computación"
 
 #Validación mayor a 0
@app.get('/uno/')
def mensaje3(edad:int):
    if edad <= 0:
        return "La edad debe ser mayor a 0"
    return f"su edad es {edad}"

@app.get('/productos/')
def listProductos():
    return productos

#Validación de existencia del producto
@app.get('/productos/{cod}')
def findProductos(cod:int): 
    for prod in productos:
        if prod['codigo']==cod:
            return prod
    return "El producto no existe"

#Validación de existencia del producto por nombre
@app.get('/productos/buscar/')
def findProductos2(nom:str): 
    for prod in productos:
        if prod['nombre']==nom:
            return prod
    return "El producto no existe"
        
#Validación siguiente consecutivo, valor y existencias mayores a 0
@app.post('/productos')
def crearProducto(cod:int, nom:str,val:float,exi:int):
    if val <= 0 or exi <= 0:
        return "El valor y las existencias deben ser mayores a 0"
    nuevo_cod = max([p['codigo'] for p in productos], default=0) + 1
    productos.append({
        'codigo': nuevo_cod, 
        'nombre': nom, 
        'valor': val, 
        'existencia': exi, 
    })
    guardar_productos()
    return productos

#Validación siguiente consecutivo, valor y existencias mayores a 0 usando Body para recibir los datos en el cuerpo de la petición
@app.post('/productos2')
def crearProducto2(
    cod:int=Body(),
    nom:str=Body(),
    val:float=Body(),
    exi:int=Body()
    ):
    if val <= 0 or exi <= 0:
        return "El valor y las existencias deben ser mayores a 0"
    nuevo_cod = max(p['codigo'] for p in productos) + 1
    productos.append({
        'codigo': nuevo_cod, 
        'nombre': nom, 
        'valor': val, 
        'existencia': exi, 
    })
    guardar_productos()
    return productos

#Validación de existencia del producto, valor y existencias mayores a 0
@app.put('/producto/{cod}')
def updateProducto(cod:int,
    nom: str=Body(),
    val:float=Body(),
    exi:int=Body()):
    for prod in productos:
        if prod['codigo']==cod:
            if val <= 0 or exi <= 0:
                return "El valor y las existencias deben ser mayores a 0"
            # Valores antes de la actualización
            antes = dict(prod)
            prod['nombre']=nom
            prod['valor']=val
            prod['existencia']=exi
            guardar_productos()
            return{"antes": antes, "despues": dict(prod)}
    return "El producto no existe"

#Validación de existencia del producto 
@app.delete('/producto/{cod}')
def deleteProducto(cod:int):
    for prod in productos:
        if prod['codigo']==cod:
            eliminado = dict(prod)
            productos.remove(prod)
            guardar_productos()
            return {"mensaje": "Producto eliminado", "producto": eliminado}
    return {"mensaje": "Producto no encontrado"}