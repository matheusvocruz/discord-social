import re
from model.social import Social
from util.settings import Settings

class Instagram(Social):
    __settings: Settings
    __parameters: str = None

    def __init__(self) -> None:
        self.__settings = Settings()
        super().__init__(self.__settings.instagram_url, self.__settings.instagram_regex)
        self.__parameters = self.__settings.instagram_paramater_regex
        pass
    
    def validate(self, message: str) -> bool:
        return re.search(self.regex, message) and re.search(self.__parameters, message)