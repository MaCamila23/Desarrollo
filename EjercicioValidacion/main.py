from fastapi import FastAPI, Path
from typing_extensions import List, Dict, Any, Dict, Union, Optional, TypedDict
from pydantic import BaseModel, Field
app=FastAPI()

productos = [
     {
        "codigo": 1,
        "nombre": "Cuaderno",
        "valoru": 5000,
        "existencias": 100
    },
         {
        "codigo": 2,
        "nombre": "Esfero",
        "valoru": 2500,
        "existencias": 250
    },
         {
        "codigo": 3,
        "nombre": "Lapiz",
        "valoru": 1500,
        "existencias": 50
    }
]

class producto(BaseModel):
    codigo: int
    nombre: str
    valoru: float
    existencias: int 

#Esquema para respuesta
class productoRespuesta(TypedDict):
    Mensaje: str
    Producto: Optional[producto]=None 

class productoCreate(BaseModel):
    codigo: int
    nombre: str=Field(min_length=5, max_length=15)
    valoru: float=Field(gt=0)
    existencias: int =Field(gt=0, le=10, default=10)


@app.get('/')
def mensaje():
    return {
        "Mensaje" : "Bienvenidos a Validaciones"
    }

#Se puede especificar el tipo de retorno
@app.get('/lista',response_model=List[producto])
def listproductos():
    return productos
@app.get('/productorespuestaAny/{cod}', response_model=Dict[str, Any])
def buscaproducto(cod:int=Path(gt=0)):
    for producto in productos:
        if producto["codigo"]==cod:
            return {
                "Mensaje" : "Produto encontrado:" ,
                "Producto: " : producto
            }
    return {
        "Mensaje" : "Producto NO encontraddo"
    }

@app.get('/productorespuestaUnion/{cod}', response_model=Dict[str,Union[str, Optional[Dict]]])
def buscaproducto(cod:int=Path(gt=0)):
    for producto in productos:
        if producto["codigo"]==cod:
            return {
                "Mensaje" : "Produto encontrado:" ,
                "Producto: " : producto
            }
    return {
        "Mensaje" : "Producto NO encontraddo" ,
        "Producto: " : None
    }
@app.get('/productorespuestaesquema/{cod}', response_model=productoRespuesta)
def buscaproducto(cod:int=Path(gt=0)):
    for producto in productos:
        if producto["codigo"]==cod:
            return productoRespuesta(
                Mensaje = "Produto encontrado:" , 
                Producto = producto
            )
    return productoRespuesta(
        Mensaje = "Produto encontrado:" , 
        Producto = None
    )

@app.post('/creaprodesquema')
def creaproducto(prod: producto):
    productos.append(prod.model_dump())
    return productos

@app.post('/creaprodesquemavalida')
def creaproducto(prod: productoCreate):
    productos.append(prod.model_dump())
    return productos

from fastapi import Body

@app.put('/producto/{cod}', response_model=productoRespuesta)
def actualizar(cod: int = Path(gt=0), prod: productoCreate = Body()):
    for p in productos:
        if p['codigo'] == cod:
            antes = dict(p)
            p['nombre'] = prod.nombre
            p['valoru'] = prod.valoru
            p['existencias'] = prod.existencias

            return {
                "Mensaje": "Producto actualizado",
                "Producto": p
            }
    return {
        "Mensaje": "El producto no existe",
        "Producto": None
    }