def test_foo():
    class CustomException(Exception):
        pass

    class SomeClass:
        def foo(self):
            raise CustomException

    # The error only appears with enough nested blocks.
    if (True == True):
        try:
            raise IOError
        except CustomException:
            pass