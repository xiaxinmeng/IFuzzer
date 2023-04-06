import unittest
from test import support
from _testcapi import Generic, GenericAlias
import test_genericclass

def test_mro_entry_signature():
    tested = []

    class B:
        ...

    class C:

        def __mro_entries__(TestMROEntry, *args, **kwargs):
            tested.extend([args, kwargs])
            return (C,)
    c = C()
    TestMROEntry.assertEqual(tested, [])

    class D(B, c):
        ...
    TestMROEntry.assertEqual(tested[0], ((B, c),))
    TestMROEntry.assertEqual(tested[1], {})

TestMROEntry = test_genericclass.TestMROEntry()
test_mro_entry_signature()
