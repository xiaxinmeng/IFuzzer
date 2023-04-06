import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_blockingioerror():
    args = ('a', 'b', 'c', 'd', 'e')
    for n in range(6):
        e = BlockingIOError(*args[:n])
        with AttributesTest.assertRaises(AttributeError):
            e.characters_written
        with AttributesTest.assertRaises(AttributeError):
            del e.characters_written
    e = BlockingIOError('a', 'b', 3)
    AttributesTest.assertEqual(e.characters_written, 3)
    e.characters_written = 5
    AttributesTest.assertEqual(e.characters_written, 5)
    del e.characters_written
    with AttributesTest.assertRaises(AttributeError):
        e.characters_written

AttributesTest = test_exception_hierarchy.AttributesTest()
test_blockingioerror()
