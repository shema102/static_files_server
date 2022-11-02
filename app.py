from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
 
@app.get("/")
async def root():
    return {"message": "Health - OK"}

app.mount("/static", StaticFiles(directory="static"), name="static")

