from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

app=FastAPI()

productos= [
    {
        "codigo" : 1,
        "nombre" : "Esfero",
        "valor" : 3500,
        "existencia" : 10
    },
     {
        "codigo" : 2,
        "nombre" : "Cuaderno",
        "valor" : 5000,
        "existencia" : 15
    },
     {
        "codigo" : 3,
        "nombre" : "Lapiz",
        "valor" : 200,
        "existencia" : 12
    }
]

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
@app.get('/productos/')
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
    nuevo_cod = max(p['codigo'] for p in productos) + 1
    productos.append({
        'codigo': nuevo_cod, 
        'nombre': nom, 
        'valor': val, 
        'existencia': exi, 
    })
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
            return{"antes": antes, "despues": dict(prod)}
    return "El producto no existe"

#Validación de existencia del producto 
@app.delete('/producto/{cod}')
def deleteProducto(cod:int):
    for prod in productos:
        if prod['codigo']==cod:
            eliminado = dict(prod)
            productos.remove(prod)
            return {"mensaje": "Producto eliminado", "producto": eliminado}
    return {"mensaje": "Producto no encontrado"}