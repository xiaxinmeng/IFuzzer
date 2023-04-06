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


@mock.patch(f"{__name__}.f", lambda: 2)
class MockedA(BaseFTests):

    def _asserts(self, val):
        print("MockedA test_a patchings : ", self.test_a.patchings)
        self.assertEqual(val, 2)
        self.assertEqual(g(), 43)


@mock.patch(f"{__name__}.g", lambda: 3)
class MockedB(MockedA):

    def _asserts(self, val):
        print("MockedB test_a patchings : ", self.test_a.patchings)
        self.assertEqual(val, g() - 1)


if __name__ == "__main__":
    unittest.main(exit=False)