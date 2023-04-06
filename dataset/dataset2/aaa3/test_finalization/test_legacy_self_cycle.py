import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

def test_legacy_LegacyFinalizationTest_cycle():
    with test_finalization.SimpleBase.test():
        s = test_finalization.LegacySelfCycle()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        LegacyFinalizationTest.assert_del_calls([])
        LegacyFinalizationTest.assert_tp_del_calls([])
        LegacyFinalizationTest.assert_survivors([])
        LegacyFinalizationTest.assert_garbage(ids)
        LegacyFinalizationTest.assertIsNot(wr(), None)
        gc.garbage[0].ref = None
    LegacyFinalizationTest.assert_garbage([])
    LegacyFinalizationTest.assertIs(wr(), None)

LegacyFinalizationTest = test_finalization.LegacyFinalizationTest()
test_legacy_LegacyFinalizationTest_cycle()
