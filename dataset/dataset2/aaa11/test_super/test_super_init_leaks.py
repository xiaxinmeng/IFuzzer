import unittest
import test_super

def test_super_init_leaks():
    sp = super(float, 1.0)
    for i in range(1000):
        super.__init__(sp, int, i)

TestSuper = test_super.TestSuper()
test_super_init_leaks()
