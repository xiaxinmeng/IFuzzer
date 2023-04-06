from abc import ABC


class A:
    def __init_subclass__(self):
        pass


class B(ABC, A, name="name"):
    pass