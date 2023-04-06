import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

@support.cpython_only
def test_non_gc():
    with test_finalization.SimpleBase.test():
        s = test_finalization.NonGC()
        SimpleFinalizationTest.assertFalse(gc.is_tracked(s))
        ids = [id(s)]
        del s
        gc.collect()
        SimpleFinalizationTest.assert_del_calls(ids)
        SimpleFinalizationTest.assert_survivors([])
        gc.collect()
        SimpleFinalizationTest.assert_del_calls(ids)
        SimpleFinalizationTest.assert_survivors([])

SimpleFinalizationTest = test_finalization.SimpleFinalizationTest()
test_non_gc()
