from fastapi import APIRouter, Depends

from controllers.data_controller import DataController
from helpers.config import Settings, get_settings


router = APIRouter(
    prefix="/api/v1/data",
    tags=["Data"],
)


def get_data_controller(
    settings: Settings = Depends(get_settings),
) -> DataController:
    return DataController(settings)
