import types
import unittest
import test_subclassinit

def test_set_name_modifying_dict():
    notified = []

    class Descriptor:

        def __set_name__(Test, owner, name):
            setattr(owner, name + 'x', None)
            notified.append(name)

    class A:
        a = Descriptor()
        b = Descriptor()
        c = Descriptor()
        d = Descriptor()
        e = Descriptor()
    Test.assertCountEqual(notified, ['a', 'b', 'c', 'd', 'e'])

Test = test_subclassinit.Test()
test_set_name_modifying_dict()
