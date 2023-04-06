class MyObject:
    def __init__(self):
        self.foo = 0
        self.bar = 0

    def set_foo(self, value):
        self.foo = value

    def set_bar(self, value):
        self.bar = value


def do_something():
    o = MyObject()
    o.set_foo(3)
    o.set_bar(4)
    return "something unrelated"


class MyObjectTest(TestCase):
    @patch(f"{__name__}.MyObject.set_bar", autospec=True)
    @patch(f"{__name__}.MyObject.set_foo", autospec=True)
    def test_do_something(self, mock_set_foo, mock_set_bar):
        manager = Mock()
        manager.attach_mock(mock_set_foo, "set_foo_func")
        manager.attach_mock(mock_set_bar, "set_bar_func")
        do_something()
        assert manager.mock_calls == [
            call.set_foo_func(ANY, 3),
            call.set_bar_func(ANY, 4),
        ]
        manager.assert_has_calls([call.set_foo_func(ANY, 3), call.set_bar_func(ANY, 4)])


if __name__ == "__main__":
    unittest.main()