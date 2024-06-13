import os
import re
from dotenv import load_dotenv

class Response:
    twitter_url: str = None
    instagram_url: str = None
    regex_twitter: str = None
    regex_instagram: str = None
    regex_instagram_param: str = None

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config/.env'))

        self.twitter_url = os.getenv('TWITTER_URL')
        self.instagram_url = os.getenv('INSTA_URL')
        self.regex_twitter = os.getenv('REGEX_TWITTER')
        self.regex_instagram = os.getenv('REGEX_INSTA')
        self.regex_instagram_param = os.getenv('REGEX_INSTA_PARAMS')
        pass


    def get_message(self, user_input: str) -> str:
        if re.search(self.regex_twitter, user_input):
            return re.sub(self.regex_twitter, self.twitter_url, user_input)
        elif re.search(self.regex_instagram, user_input) and re.search(self.regex_instagram_param, user_input):
            return re.sub(self.regex_instagram, self.instagram_url, user_input)
        else: 
            return