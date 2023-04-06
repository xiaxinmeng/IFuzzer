from collections.abc import Coroutine

class MyCoroutine(Coroutine):
    def send(self, value):
        raise StopIteration
    def throw(self, err):
        raise err

mc = MyCoroutine()