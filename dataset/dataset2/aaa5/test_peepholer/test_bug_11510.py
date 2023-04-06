import dis
import unittest
from test.support.bytecode_helper import BytecodeTestCase
import test_peepholer

def test_bug_11510():

    def f():
        (x, y) = {1, 1}
        return (x, y)
    with TestBuglets.assertRaises(ValueError):
        f()

TestBuglets = test_peepholer.TestBuglets()
test_bug_11510()
