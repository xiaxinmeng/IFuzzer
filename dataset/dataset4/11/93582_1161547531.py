# bpo93582.py

import unittest
from unittest import mock


def f():
    return 41


def g():
    return 43


class BaseFTests(unittest.TestCase):
    def test_a(self):
        self._asserts(f())

    def _asserts(self, val):
        pass


class MockedA(BaseFTests):
    def setUp(self):
        super().setUp()
        patch_f = mock.patch(f"{__name__}.f", lambda: 2)
        patch_f.start()
        self.addCleanup(patch_f.stop)

    def _asserts(self, val):
        self.assertEqual(val, 2)
        self.assertEqual(g(), 43)


class MockedB(MockedA):
    def setUp(self):
        super().setUp()
        patch_g = mock.patch(f"{__name__}.g", lambda: 3)
        patch_g.start()
        self.addCleanup(patch_g.stop)

    def _asserts(self, val):
        self.assertEqual(val, g() - 1)


if __name__ == "__main__":
    unittest.main()
