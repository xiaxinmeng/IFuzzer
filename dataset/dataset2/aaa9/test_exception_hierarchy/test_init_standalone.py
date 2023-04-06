import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_init_standalone():
    e = test_exception_hierarchy.SubOSErrorWithStandaloneInit()
    ExplicitSubclassingTest.assertEqual(e.args, ())
    ExplicitSubclassingTest.assertEqual(str(e), '')

ExplicitSubclassingTest = test_exception_hierarchy.ExplicitSubclassingTest()
test_init_standalone()
