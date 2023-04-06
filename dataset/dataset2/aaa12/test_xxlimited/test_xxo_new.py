import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_xxo_new():
    xxo = CommonTests.module.Xxo()

CommonTests = test_xxlimited.CommonTests()
test_xxo_new()
