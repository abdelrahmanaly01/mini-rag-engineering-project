from helpers.config import Settings


class BaseController:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
