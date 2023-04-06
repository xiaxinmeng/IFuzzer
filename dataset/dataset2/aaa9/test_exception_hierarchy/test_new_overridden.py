import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_new_overridden():
    e = test_exception_hierarchy.SubOSErrorWithNew('some message', 'baz')
    ExplicitSubclassingTest.assertEqual(e.baz, 'baz')
    ExplicitSubclassingTest.assertEqual(e.args, ('some message',))

ExplicitSubclassingTest = test_exception_hierarchy.ExplicitSubclassingTest()
test_new_overridden()
