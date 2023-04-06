import builtins
import unittest

class Tests(unittest.TestCase):
    def test_succeed(self):
        return

    def test_fail_once(self):
        if not hasattr(builtins, '_test_failed'):
            builtins._test_failed = True
            self.fail("bug")