import sys

class StreamWrapper(object):
    def __init__(self, wrapped):
        self.__wrapped = wrapped

    def __getattr__(self, name):
        # 'write' is overridden but for every other function, like 'flush', use the original wrapped stream
        return getattr(self.__wrapped, name)

    def write(self, text):
        pass

orig_stdout = sys.stdout
sys.stdout = StreamWrapper(orig_stdout)
print('a')   # this prints nothing
input('b')   # this should print nothing, but prints 'b' (in Python 3.5 and up only)