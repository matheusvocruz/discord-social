import re
from model.social import Social
from util.settings import Settings

class Tiktok(Social):
    __settings: Settings
    __parameters: str = None

    def __init__(self) -> None:
        self.__settings = Settings()
        super().__init__(self.__settings.tiktok_url, self.__settings.tiktok_regex)
        self.__parameters = self.__settings.tiktok_paramater_regex
        pass

    def validate(self, message: str) -> bool:
        return re.match(self.regex, message) and re.search(self.__parameters, message)