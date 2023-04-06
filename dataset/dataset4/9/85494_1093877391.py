from unittest import TestCase

class BuggyTestCase(TestCase):
    def test_generator(self):
        self.assertTrue(False)
        yield None