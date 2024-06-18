import re
from model.social import Social
from util.settings import Settings

class Reddit(Social):
    __settings: Settings

    def __init__(self) -> None:
        self.__settings = Settings()
        super().__init__(self.__settings.reddit_url, self.__settings.reddit_regex)
        pass

    def validate(self, message: str) -> bool:
        return re.search(self.regex, message)