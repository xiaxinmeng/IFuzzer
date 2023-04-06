
import unittest
from unittest import mock

class Foo:
    @classmethod
    def bar(cls, baz):
        pass

class TestFoo(unittest.TestCase):
    def test_bar(self):
        with unittest.mock.patch.object(Foo, "bar", autospec=True):
            Foo.bar()
