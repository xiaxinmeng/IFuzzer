import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

def test_simple():
    with test_finalization.SimpleBase.test():
        s = test_finalization.SimpleSelfCycle()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        SimpleFinalizationTest.assert_del_calls(ids)
        SimpleFinalizationTest.assert_survivors([])
        SimpleFinalizationTest.assertIs(wr(), None)
        gc.collect()
        SimpleFinalizationTest.assert_del_calls(ids)
        SimpleFinalizationTest.assert_survivors([])

SimpleFinalizationTest = test_finalization.SimpleFinalizationTest()
test_simple()
