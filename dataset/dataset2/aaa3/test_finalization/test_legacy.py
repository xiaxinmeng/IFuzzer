import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

def test_legacy():
    with test_finalization.SimpleBase.test():
        s = test_finalization.Legacy()
        ids = [id(s)]
        wr = weakref.ref(s)
        del s
        gc.collect()
        LegacyFinalizationTest.assert_del_calls(ids)
        LegacyFinalizationTest.assert_tp_del_calls(ids)
        LegacyFinalizationTest.assert_survivors([])
        LegacyFinalizationTest.assertIs(wr(), None)
        gc.collect()
        LegacyFinalizationTest.assert_del_calls(ids)
        LegacyFinalizationTest.assert_tp_del_calls(ids)

LegacyFinalizationTest = test_finalization.LegacyFinalizationTest()
test_legacy()
