from model.twitter import Twitter
from model.instragram import Instagram
from model.tiktok import Tiktok
from model.reddit import Reddit

class Response:
    __twitter: Twitter
    __instragram: Instagram
    __tiktok: Tiktok
    __reddit: Reddit

    def __init__(self) -> None:
        self.__twitter = Twitter()
        self.__instragram = Instagram()
        self.__tiktok = Tiktok()
        self.__reddit = Reddit()
        pass

    def build(self, message: str) -> str:
        if self.__twitter.validate(message): return self.__twitter.format(message)
        elif self.__instragram.validate(message): return self.__instragram.format(message)
        elif self.__tiktok.validate(message): return self.__tiktok.format(message)
        elif self.__reddit.validate(message): return self.__reddit.format(message)
        else: return