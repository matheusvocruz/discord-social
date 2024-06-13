import os
import re
from dotenv import load_dotenv
from model.social import Social

class Twitter(Social):
    def __init__(self) -> None:
        load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config/.env'))
        super().__init__(os.getenv('TWITTER_URL'), os.getenv('REGEX_TWITTER'))
        pass

    def validate(self, message: str) -> bool:
        return re.search(self.regex, message)