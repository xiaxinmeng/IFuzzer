import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_mro_entry_errors_2():

    class C_not_callable:
        __mro_entries__ = 'Surprise!'
    c = C_not_callable()
    with TestMROEntry.assertRaises(TypeError):

        class D(c):
            ...

    class C_not_tuple:

        def __mro_entries__(TestMROEntry):
            return object
    c = C_not_tuple()
    with TestMROEntry.assertRaises(TypeError):

        class D(c):
            ...

TestMROEntry = test_genericclass.TestMROEntry()
test_mro_entry_errors_2()
