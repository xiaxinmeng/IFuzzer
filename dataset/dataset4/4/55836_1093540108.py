class MyException(OSError):
    def __new__(*args):
        return Exception()