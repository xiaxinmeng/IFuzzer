from unittest.mock import MagicMock, create_autospec, patch

class SomeClass(object):

    def some_method(self):
        print("Hi!")

if __name__ == "__main__":
    ins = SomeClass()
    assert ins.some_method.__qualname__ == "SomeClass.some_method"

    with patch('__main__.SomeClass', autospec=True) as mocked:
        obj = SomeClass()
        assert obj.some_method.__qualname__ == "SomeClass.some_method"
        obj.some_method()
        obj.some_method.assert_called_once()