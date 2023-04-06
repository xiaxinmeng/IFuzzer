
from threading import Thread
from contextvars import ContextVar

foo: ContextVar[str] = ContextVar("foo")


def temp():
    print(foo.get())


foo.set("bar")

t = Thread(target=temp)
t.start()
t.join()
