import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

def test_simple_suicide():
    with test_finalization.SimpleBase.test():
        s = test_finalization.SuicidalSelfCycle()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        SelfCycleFinalizationTest.assert_del_calls(ids)
        SelfCycleFinalizationTest.assert_survivors([])
        SelfCycleFinalizationTest.assertIs(wr(), None)
        gc.collect()
        SelfCycleFinalizationTest.assert_del_calls(ids)
        SelfCycleFinalizationTest.assert_survivors([])
        SelfCycleFinalizationTest.assertIs(wr(), None)

SelfCycleFinalizationTest = test_finalization.SelfCycleFinalizationTest()
test_simple_suicide()
