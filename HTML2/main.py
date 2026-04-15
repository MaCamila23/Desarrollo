
from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
async def pagina_inicio():
    return FileResponse("templates/index.html") 