from helpers.config import get_settings
import os 
import random
import string

class BaseController:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.files_dir = os.path.join(self.base_dir, "assets", "files")
        
        
    def generate_random_string(self, length: int = 8) -> str:
        """Generate a random string of specified length."""
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))  