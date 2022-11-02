from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
 
@app.get("/")
async def root():
    return {"message": "Static files server"}

app.mount("/static", StaticFiles(directory="static"), name="static")

