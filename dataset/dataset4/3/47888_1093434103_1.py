import _tkinter

def bad():
    raise InvalidThing

x = _tkinter.create()
x.createcommand("bad", bad)
x.call("bad")