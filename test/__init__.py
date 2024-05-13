import unittest


class BaseTestClass(unittest.TestCase):

    # Code that is executed before each test
    def setUp(self):
        self.api = 'https://example.com'
