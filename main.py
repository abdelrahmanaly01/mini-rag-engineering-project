from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv('.env')
from routes.base import router


app = FastAPI()
app.include_router(router)

