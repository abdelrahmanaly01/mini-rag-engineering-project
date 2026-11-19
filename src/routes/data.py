from fastapi import APIRouter, File, UploadFile

from controllers.data_controller import DataController


router = APIRouter(
    prefix="/api/v1/data",
    tags=["Data"],
)


@router.post("/upload/{file_id}")
async def upload_file(
    file_id: str,
    file: UploadFile = File(...),
):
    data_controller = DataController()
    return data_controller.validate_file(file)