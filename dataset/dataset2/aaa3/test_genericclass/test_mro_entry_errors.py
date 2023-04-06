import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_mro_entry_errors():

    class C_too_many:

        def __mro_entries__(TestMROEntry, bases, something, other):
            return ()
    c = C_too_many()
    with TestMROEntry.assertRaises(TypeError):

        class D(c):
            ...

    class C_too_few:

        def __mro_entries__(TestMROEntry):
            return ()
    d = C_too_few()
    with TestMROEntry.assertRaises(TypeError):

        class D(d):
            ...

TestMROEntry = test_genericclass.TestMROEntry()
test_mro_entry_errors()
