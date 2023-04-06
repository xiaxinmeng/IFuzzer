from unittest import TestCase
from unittest.mock import patch

import inspect

class TestClass(TestCase):
    def setUp(self):
        patcher = patch('inspect.isfunction')
        self.addCleanup(patcher.stop)
        self.patched_func = patcher.start()

    def test_m(self):
        def f():
           pass

        inspect.isfunction(f)