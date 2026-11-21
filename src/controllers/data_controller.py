from fastapi import UploadFile

from controllers.base_controller import BaseController
from models.enums.responseEnums import FileUploadResponse


class DataController(BaseController):
    def validate_file(self, file: UploadFile) -> dict[str, bool | str]:
        file_type = (file.content_type or "").lower()
        allowed_types = {
            allowed_type.lower() for allowed_type in self.settings.ALLOWED_FILE_TYPES
        }
        if file_type not in allowed_types:
            return {
                "valid": False,
                "message": FileUploadResponse.FILE_TYPE_NOT_SUPPORTED.value,
            }

        if file.size is not None and file.size > self.settings.MAX_FILE_SIZE*1024*1024:
            return {
                "valid": False,
                "message": FileUploadResponse.FILE_EXCEEDS_MAX_SIZE.value,
            }

        return {
            "valid": True,
            "message": FileUploadResponse.FILE_SUPPORTED.value,
        }
