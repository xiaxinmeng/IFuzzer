import io
import sys


class Writer:
    def __getattr__(self, name):
        return getattr(sys.__stdout__, name)

    def write(self, data):
        if data != '\n':
            sys.__stdout__.write('Wrapped stdout\n')

    def fileno():
        raise OSError()


class Reader:
    def __getattr__(self, name):
        return getattr(sys.__stdin__, name)

    def read(self, size):
        return sys.__stdin__.read(size)

    def fileno():
        raise OSError()


sys.stdout = Writer()
sys.stdin = Reader()

print('print')
input('input')