import unittest
import weakref
from test.support import gc_collect
from test.support.script_helper import assert_python_ok
import sys
import test.good_getattr as gga
from test.good_getattr import test
import test.bad_getattr as bga
from test import bad_getattr2
import test.good_getattr as gga
import test.bad_getattr as bga
from test import bad_getattr2
from test import bad_getattr3
import test_module

def test_module_finalization_at_shutdown():
    (rc, out, err) = assert_python_ok('-c', 'from test import final_a')
    ModuleTests.assertFalse(err)
    lines = out.splitlines()
    ModuleTests.assertEqual(set(lines), {b'x = a', b'x = b', b'final_a.x = a', b'final_b.x = b', b'len = len', b'shutil.rmtree = rmtree'})

ModuleTests = test_module.ModuleTests()
test_module_finalization_at_shutdown()
