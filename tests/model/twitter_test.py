import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/'))) # get src classes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # get Mock
from model.twitter import Twitter 
from tests.mock import Mock

class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.__twitter = Twitter()

    def test_validate_x_successfully(self):
        self.assertTrue(self.__twitter.validate(Mock.get_x_url()))

    def test_validate_twitter_successfully(self):
        self.assertTrue(self.__twitter.validate(Mock.get_twitter_url()))

    def test_validate_error(self):
        self.assertFalse(self.__twitter.validate(Mock.get_random_url()))

    def test_format_x_successfully(self):
        self.assertNotEqual(Mock.get_x_url(), self.__twitter.format(Mock.get_x_url()))

    def test_format_twitter_successfully(self):
        self.assertNotEqual(Mock.get_twitter_url(), self.__twitter.format(Mock.get_twitter_url()))

    def test_format_error(self):
        self.assertEqual(Mock.get_random_url(), self.__twitter.format(Mock.get_random_url()))

if __name__ == '__main__':
    unittest.main()