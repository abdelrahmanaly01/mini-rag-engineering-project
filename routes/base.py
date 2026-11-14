from fastapi import FastAPI, APIRouter

import os


router = APIRouter(
    prefix="/api/v1",
    tags=["Base"],
    
    
)

@router.get("/")
async def read_root():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {"message": "Welcome to the API!",
            "app_name": app_name, 
            "app_version": app_version}