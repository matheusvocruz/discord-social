import unittest
from src.model.twitter import Twitter 

class TwitterTest(unittest.TestCase):
    def validate_x_successfully() -> None:
        assert(Twitter().validate('https://x.com/MoviesAndchills/status/1803369329129357665'))

    def validate_twitter_successfully() -> None:
        assert(Twitter().validate('https://x.com/MoviesAndchills/status/1803369329129357665'))
