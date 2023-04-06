import unittest
from test import ann_module, support
import test_opcodes

def test_use_existing_annotations():
    ns = {'__annotations__': {1: 2}}
    exec('x: int', ns)
    OpcodeTest.assertEqual(ns['__annotations__'], {'x': 'int', 1: 2})

OpcodeTest = test_opcodes.OpcodeTest()
test_use_existing_annotations()
