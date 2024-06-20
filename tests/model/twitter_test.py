import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/')))
from model.twitter import Twitter 

class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.__twitter = Twitter() 
        pass

    def test_validate_x_successfully(self):
        self.assertTrue(self.__twitter.validate('https://x.com/user/status/1803369329129357665'))

    def test_validate_twitter_successfully(self):
        self.assertTrue(self.__twitter.validate('https://x.com/user/status/1803369329129357665'))

if __name__ == '__main__':
    unittest.main()