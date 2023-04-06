import unittest
from unittest.mock import patch, Mock, call, ANY


class Foo:
    def set_foo(self, val): pass


class FooTest(unittest.TestCase):
    @patch(f"{__name__}.Foo.set_foo", autospec=True)
    def test_autospec_attach_mock_assert(self, mock_set_foo):
        manager = Mock()
        manager.attach_mock(mock_set_foo, "set_foo_func")
        obj = Foo()
        obj.set_foo(3)
        manager.assert_has_calls([call.set_foo_func(ANY, 3)])

if __name__ == "__main__":
    unittest.main()