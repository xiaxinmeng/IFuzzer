import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_cell_new():
    cell_obj = types.CellType(1)
    FunctionPropertiesTest.assertEqual(cell_obj.cell_contents, 1)
    cell_obj = types.CellType()
    msg = "shouldn't be able to read an empty cell"
    with FunctionPropertiesTest.assertRaises(ValueError, msg=msg):
        cell_obj.cell_contents

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
test_cell_new()
