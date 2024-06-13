import os
from dotenv import load_dotenv

class Settings:
    token: str = None
    twitter_url: str = None
    instagram_url: str = None
    twitter_regex: str = None
    instagram_regex: str = None
    instagram_paramater_regex: str = None

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config/.env'))

        self.__build_discord()
        self.__build_twitter()
        self.__build_instagram()
        pass

    def __build_discord(self) -> None:
        self.token = os.getenv('DISCORD_TOKEN')

    def __build_twitter(self) -> None:
        self.twitter_url = os.getenv('TWITTER_URL')
        self.twitter_regex = os.getenv('TWITTER_REGEX')

    def __build_instagram(self) -> None:
        self.instagram_url = os.getenv('INSTAGRAM_URL')
        self.instagram_regex = os.getenv('INSTAGRAM_REGEX')
        self.instagram_paramater_regex = os.getenv('INSTAGRAM_PARAMETER_REGEX')