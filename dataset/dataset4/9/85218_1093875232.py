
import unittest

class MyTestCase(unittest.TestCase):

    @classmethod
    def ready_for_tests(cls):
        pass

    @classmethod
    def setUpClass(cls):
        if not cls.ready_for_tests():
            cls.skipTest()
