import unittest
import builtins
import os
from platform import system as platform_system
import test_baseexception

def test_interface_no_arg():
    exc = Exception()
    results = ([len(exc.args), 0], [exc.args, tuple()], [str(exc), ''], [repr(exc), exc.__class__.__name__ + '()'])
    ExceptionClassTests.interface_test_driver(results)

ExceptionClassTests = test_baseexception.ExceptionClassTests()
test_interface_no_arg()
