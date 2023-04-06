import inspect
import unittest

class TestIsclass(unittest.TestCase):
    def test_instance_with_getattr(self):
        class Cls:
            def __getattr__(self, name):
                return "not important"
        obj = Cls()
        # obj is not a class
        self.failIf(inspect.isclass(obj))