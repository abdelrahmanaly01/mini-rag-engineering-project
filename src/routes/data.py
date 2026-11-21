from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse
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
    result = data_controller.validate_file(file)
    return JSONResponse(
        content=result,
        status_code=status.HTTP_200_OK if result["valid"] else status.HTTP_400_BAD_REQUEST,
        media_type="application/json",
    )