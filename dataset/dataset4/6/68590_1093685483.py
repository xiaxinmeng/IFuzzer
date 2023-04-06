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


sys.stdout = Writer()

print('print')
input('input')