import os
from dotenv import load_dotenv

class Settings:
    token: str = None
    twitter_url: str = None
    instagram_url: str = None
    tiktok_url: str = None
    reddit_url: str = None
    twitter_regex: str = None
    instagram_regex: str = None
    tiktok_regex: str = None
    reddit_regex: str = None
    instagram_paramater_regex: str = None
    tiktok_paramater_regex: str = None

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../docs/.env'))

        self.__build_discord()
        self.__build_twitter()
        self.__build_instagram()
        self.__build_tiktok()
        self.__build_reddit()
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

    def __build_tiktok(self) -> None:
        self.tiktok_url = os.getenv('TIKTOK_URL')
        self.tiktok_regex = os.getenv('TIKTOK_REGEX')
        self.tiktok_paramater_regex = os.getenv('TIKTOK_PARAMETER_REGEX')

    def __build_reddit(self) -> None:
        self.reddit_url = os.getenv('REDDIT_URL')
        self.reddit_regex = os.getenv('REDDIT_REGEX')