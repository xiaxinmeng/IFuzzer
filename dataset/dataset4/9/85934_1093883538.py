import unittest
from unittest.mock import Mock

class SomethingElse(object):
    def __init__(self):
        self._instance = None

    @property
    def instance(self):
        if not self._instance:
            self._instance = 'object'

class Test(unittest.TestCase):

    def test_property_not_called_with_spec_mock(self):
        obj = SomethingElse()
        self.assertIsNone(obj._instance, msg='before') # before
        mock = Mock(spec=obj)
        self.assertIsNone(obj._instance, msg='after') # after

unittest.main()