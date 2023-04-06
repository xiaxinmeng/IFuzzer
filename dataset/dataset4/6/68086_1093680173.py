class MySpecialObject(object):

    def __eq__(self, other):
        return MySpecialObject()

    def __bool__(self):
        raise NotImplementedError(
            "This object does not specify a boolean value")


class MyClass(object):
    some_thing = MySpecialObject()

import inspect

print(inspect.classify_class_attrs(MyClass))