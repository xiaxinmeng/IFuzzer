import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_bpo_42057():
    for i in range(10):
        try:
            raise Exception
        except Exception or Exception:
            pass

TestBuglets = test_peepholer.TestBuglets()
test_bpo_42057()
