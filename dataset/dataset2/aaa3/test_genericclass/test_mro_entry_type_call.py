import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_mro_entry_type_call():

    class C:

        def __mro_entries__(TestMROEntry, bases):
            return ()
    c = C()
    with TestMROEntry.assertRaisesRegex(TypeError, 'MRO entry resolution; use types.new_class()'):
        type('Bad', (c,), {})

TestMROEntry = test_genericclass.TestMROEntry()
test_mro_entry_type_call()
