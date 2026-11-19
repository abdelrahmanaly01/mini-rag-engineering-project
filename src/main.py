from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv('.env')
from routes.data import router as data_router
from routes.base import router


app = FastAPI()
app.include_router(router)
app.include_router(data_router)

