import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

def test_simple_resurrect():
    with test_finalization.SimpleBase.test():
        s = test_finalization.SelfCycleResurrector()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        SimpleFinalizationTest.assert_del_calls(ids)
        SimpleFinalizationTest.assert_survivors(ids)
        SimpleFinalizationTest.assertIs(wr(), None)
        SimpleFinalizationTest.clear_survivors()
        gc.collect()
        SimpleFinalizationTest.assert_del_calls(ids)
        SimpleFinalizationTest.assert_survivors([])
        SimpleFinalizationTest.assertIs(wr(), None)

SimpleFinalizationTest = test_finalization.SimpleFinalizationTest()
test_simple_resurrect()
