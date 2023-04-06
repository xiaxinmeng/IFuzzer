import warnings
warn = warnings.warn

class A:
    def __del__(self):
        warn("bla")

a=A()