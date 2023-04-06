import unittest
from unittest import TestCase

class BuggyTestCase(TestCase):

    def _callTestMethod(self, method):
        import inspect

        if inspect.isgeneratorfunction(method):
            list(method())
        else:
            method()

    def test_generator(self):
        self.assertTrue(False)
        yield None

if __name__ == "__main__":
    unittest.main()