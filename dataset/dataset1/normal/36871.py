# python3

import unittest
from unittest import mock


class Thing(object):

    def __init__(self, constructor_param):
        self._xxx = constructor_param

    def method(self, a=None, b=0):
        print(f"a = {a} b = {b}")


class MockCallTest(unittest.TestCase):

    def test_has_calls_on_thing(self):
        print("Thing:", Thing)
        mock_thing = mock.create_autospec(Thing)
        print(f"mock_thing.method sig={mock_thing.method._spec_signature}")
        mock_thing.method(0.5, b=3000)
        mock_thing.method(0.6, b=6000)
        mock_thing.method(0.7, b=9000)
        mock_thing.assert_has_calls([
            mock.call.method(0.5, b=3000),
            mock.call.method(0.6, b=6000),
            mock.call.method(0.7, b=9000),
        ])


if __name__ == "__main__":
    unittest.main()
