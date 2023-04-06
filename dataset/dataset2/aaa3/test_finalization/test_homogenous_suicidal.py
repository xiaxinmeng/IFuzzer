import contextlib
import gc
import unittest
import weakref
from _testcapi import with_tp_del
from _testcapi import without_gc
from test import support
import test_finalization

def test_homogenous_suicidal():
    CycleChainFinalizationTest.check_non_resurrecting_chain([test_finalization.SuicidalChained] * 3)

CycleChainFinalizationTest = test_finalization.CycleChainFinalizationTest()
test_homogenous_suicidal()
