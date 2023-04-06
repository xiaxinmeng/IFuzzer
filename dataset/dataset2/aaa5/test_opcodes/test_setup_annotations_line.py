import unittest
from test import ann_module, support
import test_opcodes

def test_setup_annotations_line():
    try:
        with open(ann_module.__file__) as f:
            txt = f.read()
        co = compile(txt, ann_module.__file__, 'exec')
        OpcodeTest.assertEqual(co.co_firstlineno, 1)
    except OSError:
        pass

OpcodeTest = test_opcodes.OpcodeTest()
test_setup_annotations_line()
