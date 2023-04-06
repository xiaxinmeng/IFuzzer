import unittest
import builtins
import os
from platform import system as platform_system
import test_baseexception

def test_catch_non_BaseException():

    class NonBaseException(object):
        pass
    UsageTests.catch_fails(NonBaseException)
    UsageTests.catch_fails(NonBaseException())

UsageTests = test_baseexception.UsageTests()
test_catch_non_BaseException()
