import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_init_kwdargs():
    e = test_exception_hierarchy.SubOSErrorWithInit('some message', bar='baz')
    ExplicitSubclassingTest.assertEqual(e.bar, 'baz')
    ExplicitSubclassingTest.assertEqual(e.args, ('some message',))

ExplicitSubclassingTest = test_exception_hierarchy.ExplicitSubclassingTest()
test_init_kwdargs()
