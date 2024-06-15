import re
from abc import ABC, abstractmethod

class Social(ABC):
    url: str = None
    regex: str = None

    def __init__(self, url: str, regex: str) -> None:
        self.url = url
        self.regex = regex
        pass
    
    @abstractmethod
    def validate(self, message: str) -> bool:
        pass
    
    def format(self, message: str) -> str:
        return re.sub(self.regex, self.url, message)