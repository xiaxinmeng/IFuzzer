import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_comparison():
    CellTest.assertTrue(test_funcattrs.cell(2) < test_funcattrs.cell(3))
    CellTest.assertTrue(test_funcattrs.empty_cell() < test_funcattrs.cell('saturday'))
    CellTest.assertTrue(test_funcattrs.empty_cell() == test_funcattrs.empty_cell())
    CellTest.assertTrue(test_funcattrs.cell(-36) == test_funcattrs.cell(-36.0))
    CellTest.assertTrue(test_funcattrs.cell(True) > test_funcattrs.empty_cell())

CellTest = test_funcattrs.CellTest()
test_comparison()
