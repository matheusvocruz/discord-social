from typing import Final
import os
from dotenv import load_dotenv
import re

load_dotenv()
TWITTER_URL: Final[str] = os.getenv('TWITTER_URL')
REGEX_TWITTER: Final[str] = os.getenv('REGEX_TWITTER')
INSTA_URL: Final[str] = os.getenv('INSTA_URL')
REGEX_INSTA: Final[str] = os.getenv('REGEX_INSTA')
REGEX_INSTA_PARAMS: Final[str] = os.getenv('REGEX_INSTA_PARAMS')

def get_response(user_input: str) -> str:
    if re.search(REGEX_TWITTER, user_input):
        return re.sub(REGEX_TWITTER, TWITTER_URL, user_input)
    elif re.search(REGEX_INSTA, user_input) and re.search(REGEX_INSTA_PARAMS, user_input):
        return re.sub(REGEX_INSTA, INSTA_URL, user_input)
    else: 
        return