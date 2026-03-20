from fastapi import FastAPI, Body

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

#@app.get('/{nombre}/{codigo}')
#def mensaje2(nombre:str,codigo:int):
#   return f"Bienvenido {nombre}, su codigo es: {codigo}"

@app.get('/uno/')
def mensaje3(edad:int):
    return f"su edad es {edad}"

@app.get('/productos/')
def listProductos():
    return productos

@app.get('/productos/{cod}')
def findProductos(cod:int): 
    for prod in productos:
        if cod['codigo']==cod:
            return prod

@app.get('/productos/')
def findProductos2(nom:str): 
    for prod in productos:
        if prod['nombre']==nom:
            return prod
        
@app.post('/productos')
def crearProducto(cod:int, nom:str,val:float,exi:int):
    productos.append({
        'codigo': cod, 
        'nombre': nom, 
        'valor': val, 
        'existenicas': exi, 
    })
    return productos

@app.post('/productos2')
def crearProducto2(
    cod:int=Body(),
    nom:str=Body(),
    val:float=Body(),
    exi:int=Body()
    ):
    productos.append({
        'codigo': cod, 
        'nombre': nom, 
        'valor': val, 
        'existenicas': exi, 
    })
    return productos

@app.put('/producto/{cod}')
def updateProducto(cod:int,
    nom: str=Body(),
    val:float=Body(),
    exi:int=Body()):
    for prod in productos:
        if prod['codigo']==cod:
            prod['nombre']=nom
            prod['valor']=val
            prod['existencia']=exi
    return productos

@app.delete('/producto/{cod}')
def deleteProducto(cod:int):
    for prod in productos:
        if prod['codigo']==cod:
            productos.remove(prod)
    return productos