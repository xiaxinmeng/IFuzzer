import weakref

class Object:
    def __init__(self, arg):
        self.arg = arg

def test_set_callback_attribute():
    x = Object(1)
    callback = lambda ref: None
    callback = weakref.ref(callback, x)
    with test_set_callback_attribute():
        pass

test_set_callback_attribute()