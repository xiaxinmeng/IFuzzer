from PySide2 import QtCore

class MyQObject(QtCore.QObject):
    sig = QtCore.Signal()

async def demo():
    myqobject = MyQObject()
    myqobject.sig.connect(lambda: None)
    return 1

coro = demo()
try:
    coro.send(None)
except StopIteration as exc:
    print(f"OK: got {exc!r}")
except SystemError as exc:
    print(f"WTF: got {exc!r}")