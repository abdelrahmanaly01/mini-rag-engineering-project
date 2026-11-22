import os

from fastapi import UploadFile
from controllers.base_controller import BaseController
from models import FileUploadResponse
from controllers import project_controller
import re



class DataController(BaseController):
    def validate_file(self, file: UploadFile, project_id: str) -> dict[str, bool | str]:
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

    def generate_unique_filename(self, original_filename: str, project_id: str) -> str:
        """
        Generates a unique filename by appending a random string to the original filename.
        Args:
            original_filename (str): The original filename.
        Returns:
            str: A unique filename.
        """
        project_path = project_controller.ProjectController().get_project_info(project_id)
        random_string = self.generate_random_string()
        cleaned_filename = self.get_clean_filename(original_filename)
        new_file_name = f"{random_string}_{cleaned_filename}"
        while os.path.exists(os.path.join(project_path, f"{random_string}_{cleaned_filename}")):
            random_string = self.generate_random_string()
            new_file_name = f"{random_string}_{cleaned_filename}"
        new_file_path = os.path.join(project_path, new_file_name)
        return new_file_path

    def get_clean_filename(self, filename: str) -> str:
        """
        Cleans the filename by removing unwanted characters and normalizing it.
        Args:
            filename (str): The original filename.
        Returns:
            str: The cleaned filename.
        """
        # Remove any characters that are not alphanumeric, dots, or underscores
        filename = re.sub(r'[^\w\.]', '_', filename)
        # Normalize the filename
        filename = filename.strip()
        return filename