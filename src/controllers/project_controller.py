from controllers.base_controller import BaseController
import os
class ProjectController(BaseController):
    def get_project_info(self, project_id: str):
        """
        Retrieves the directory path for a given project ID. If the project directory does not exist, it creates one.
        Returns:
            str: The directory path for the project.
        """
        project_path = os.path.join(self.files_dir, project_id)
        if os.path.exists(project_path):
            return os.path.dirname(project_path)
        else:
            os.makedirs(project_path)
            return os.path.dirname(project_path)