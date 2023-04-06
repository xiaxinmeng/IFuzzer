import types
import unittest
import test_subclassinit

def test_set_name_lookup():
    resolved = []

    class NonDescriptor:

        def __getattr__(Test, name):
            resolved.append(name)

    class A:
        d = NonDescriptor()
    Test.assertNotIn('__set_name__', resolved, '__set_name__ is looked up in instance dict')

Test = test_subclassinit.Test()
test_set_name_lookup()
