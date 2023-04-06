import inspect

# userland descriptor
class Descriptor(object):
    def __get__(self, instance, owner):
        if instance is None:
            return self
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass

# class with property + userland descriptor
class X(object):
    @property
    def foo(self):
        pass
    @foo.deleter
    def foo(self):
        pass

    bar = Descriptor()

# property.__delete__ and Descriptor.__delete__ both accept two arguments:
property.__delete__(X.foo, X())
Descriptor.__delete__(X.bar, X())