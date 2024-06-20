import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/'))) # get src classes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # get Mock
from model.reddit import Reddit 
from tests.mock import Mock

class RedditTest(unittest.TestCase):
    def setUp(self):
        self.__reddit = Reddit()

    def test_validate_successfully(self):
        self.assertTrue(self.__reddit.validate(Mock.get_reddit_url()))

    def test_validate_error(self):
        self.assertFalse(self.__reddit.validate(Mock.get_random_url()))

    def test_format_successfully(self):
        self.assertNotEqual(Mock.get_reddit_url(), self.__reddit.format(Mock.get_reddit_url()))

    def test_format_error(self):
        self.assertEqual(Mock.get_random_url(), self.__reddit.format(Mock.get_random_url()))

if __name__ == '__main__':
    unittest.main()