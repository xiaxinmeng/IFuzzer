import unittest
import builtins
import os
from platform import system as platform_system
import test_baseexception

def test_builtins_new_style():
    ExceptionClassTests.assertTrue(issubclass(Exception, object))

ExceptionClassTests = test_baseexception.ExceptionClassTests()
test_builtins_new_style()
