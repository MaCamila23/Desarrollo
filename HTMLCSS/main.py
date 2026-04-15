from fastapi import FastAPI
from fastapi.responses import FileResponse, StaticFiles
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name=static)

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html","r", encoding="utf-8") as file:
        return html_content
    return FileResponse("templates/index.html") 
