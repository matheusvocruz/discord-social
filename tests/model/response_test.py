import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/'))) # get src classes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # get Mock
from model.response import Response 
from tests.mock import Mock

class ResponseTest(unittest.TestCase):
    def setUp(self):
        self.__response = Response()

    def test_build_twitter_successfully(self):
        self.assertNotEqual(Mock.get_twitter_url(), self.__response.build(Mock.get_twitter_url()))

    def test_build_instagram_successfully(self):
        self.assertNotEqual(Mock.get_instagram_url(), self.__response.build(Mock.get_instagram_url()))

    def test_build_reddit_successfully(self):
        self.assertNotEqual(Mock.get_reddit_url(), self.__response.build(Mock.get_reddit_url()))

    def test_build_tiktok_successfully(self):
        self.assertNotEqual(Mock.get_tiktok_url(), self.__response.build(Mock.get_tiktok_url()))

    def test_build_error(self):
        self.assertFalse(self.__response.build(Mock.get_random_url()))

if __name__ == '__main__':
    unittest.main()