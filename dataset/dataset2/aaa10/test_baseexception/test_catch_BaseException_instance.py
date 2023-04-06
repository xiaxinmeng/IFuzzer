import unittest
import builtins
import os
from platform import system as platform_system
import test_baseexception

def test_catch_BaseException_instance():
    UsageTests.catch_fails(BaseException())

UsageTests = test_baseexception.UsageTests()
test_catch_BaseException_instance()
