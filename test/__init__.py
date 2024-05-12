import unittest
from test.assert_general import AssertGeneral


class BaseTestClass(unittest.TestCase, AssertGeneral):

    # Code that is executed before each test
    def setUp(self):
        self.api = 'https://example.com'
