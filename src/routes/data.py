import os
from helpers.config import Settings, get_settings
from fastapi import APIRouter, Depends
from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse
from controllers import DataController, project_controller
import aiofiles
from models import FileUploadResponse
router = APIRouter(
    prefix="/api/v1/data",
    tags=["Data"],
)


@router.post("/upload/{project_id}")
async def upload_file(
    project_id: str,
    file: UploadFile = File(...),settings: Settings = Depends(get_settings)
):
    data_controller = DataController()
    result = data_controller.validate_file(file,project_id)
    
    if result["valid"]:

        project_path = project_controller.ProjectController().get_project_info(project_id)
        file_path = data_controller.generate_unique_filename(str(file.filename), project_id)
        async with aiofiles.open(file_path, "wb") as out_file:
            while chunk_content := await file.read(settings.MAX_CHUNK_SIZE):
                await out_file.write(chunk_content)
        return JSONResponse(
            content={"message": FileUploadResponse.FILE_UPLOAD_SUCCESS.value},
            media_type="application/json",
        )
    else:
        return JSONResponse(
            content=result,
            status_code=status.HTTP_400_BAD_REQUEST,
            media_type="application/json",
        )      

    

    
    