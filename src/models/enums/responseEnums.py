from enum import Enum


class FileUploadResponse(str, Enum):
    FILE_TYPE_NOT_SUPPORTED = "File type is not supported."
    FILE_EXCEEDS_MAX_SIZE = "File exceeds the maximum allowed size."
    FILE_SUPPORTED = "File is supported."
    FILE_UPLOAD_SUCCESS = "File uploaded successfully."
