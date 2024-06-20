import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/'))) # get src classes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) # get Mock
from model.tiktok import Tiktok 
from tests.mock import Mock

class TiktokTest(unittest.TestCase):
    def setUp(self):
        self.__tiktok = Tiktok()

    def test_validate_successfully(self):
        self.assertTrue(self.__tiktok.validate(Mock.get_tiktok_url()))

    def test_validate_error(self):
        self.assertFalse(self.__tiktok.validate(Mock.get_random_url()))

    def test_format_successfully(self):
        self.assertNotEqual(Mock.get_tiktok_url(), self.__tiktok.format(Mock.get_tiktok_url()))

    def test_format_error(self):
        self.assertEqual(Mock.get_random_url(), self.__tiktok.format(Mock.get_random_url()))

if __name__ == '__main__':
    unittest.main()