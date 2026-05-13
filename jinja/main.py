
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    return RedirectResponse(url="/usuario/Invitado")

@app.get("/usuario/{nombre}")
async def usuario(request: Request, nombre: str, edad: int = 25, casado: bool=False):
    datos = {
        "request": request,
        "nombre": nombre,
        "edad": edad,
        "casado": casado,  
        "hobbies": ["Viajes", "Programar", "Música"]
    }
    return templates.TemplateResponse("index.html", datos)

