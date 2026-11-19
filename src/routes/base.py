from fastapi import APIRouter, Depends
from helpers.config import Settings, get_settings


router = APIRouter(
    prefix="/api/v1",
    tags=["Base"],
)


@router.get("/")
async def read_root(settings: Settings = Depends(get_settings)):
    app_name = settings.APP_NAME
    app_version = settings.APP_VERSION
    return {
        "message": "Welcome to the API!",
        "app_name": app_name,
        "app_version": app_version,
    }