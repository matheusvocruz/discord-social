from model.twitter import Twitter
from model.instragram import Instagram

class Response:
    __twitter: Twitter
    __instragram: Instagram

    def __init__(self) -> None:
        self.__twitter = Twitter()
        self.__instragram = Instagram()
        pass

    def get_message(self, user_input: str) -> str:
        if self.__twitter.validate(user_input): return self.__twitter.format(user_input)
        elif self.__instragram.validate(user_input): return self.__instragram.format(user_input)
        else: return