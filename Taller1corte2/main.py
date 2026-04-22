from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def inventario(request: Request):

    productos = [
        {"codigo": 1, "nombre": "Cuaderno", "valoru": 5000, "existencias": 100},
        {"codigo": 2, "nombre": "Esfero", "valoru": 2500, "existencias": 250},
        {"codigo": 3, "nombre": "Lapiz", "valoru": 1500, "existencias": 300},
    ]

    
    for p in productos:
        p["valor_total"] = p["valoru"] * p["existencias"]

        if p["existencias"] < 50:
            p["estado"] = "Bajo"
            p["clase"] = "bajo"
        elif 50 <= p["existencias"] <= 100:
            p["estado"] = "Medio"
            p["clase"] = "medio"
        else:
            p["estado"] = "Alto"
            p["clase"] = "alto"

    return templates.TemplateResponse("index.html", {
    "request": request,
    "productos": productos
})