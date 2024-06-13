from model.twitter import Twitter
from model.instragram import Instagram

class Response:
    twitter: Twitter
    instragram: Instagram

    def __init__(self) -> None:
        self.twitter = Twitter()
        self.instragram = Instagram()
        pass

    def get_message(self, user_input: str) -> str:
        if self.twitter.validate(user_input): return self.twitter.format(user_input)
        elif self.instragram.validate(user_input): return self.instragram.format(user_input)
        else: return