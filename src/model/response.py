from model.twitter import Twitter
from model.instragram import Instagram

class Response:
    __twitter: Twitter
    __instragram: Instagram

    def __init__(self) -> None:
        self.__twitter = Twitter()
        self.__instragram = Instagram()
        pass

    def build(self, message: str) -> str:
        if self.__twitter.validate(message): return self.__twitter.format(message)
        elif self.__instragram.validate(message): return self.__instragram.format(message)
        else: return