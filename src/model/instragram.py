import os
import re
from dotenv import load_dotenv
from model.social import Social

class Instagram(Social):
    parameters: str = None

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config/.env'))
        super().__init__(os.getenv('INSTA_URL'), os.getenv('REGEX_INSTA'))
        self.parameters = os.getenv('REGEX_INSTA_PARAMS')
        pass
    
    def validate(self, message: str) -> bool:
        return re.search(self.parameters, message) and re.search(self.parameters, message)