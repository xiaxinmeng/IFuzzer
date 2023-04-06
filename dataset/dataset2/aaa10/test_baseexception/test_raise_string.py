import unittest
import builtins
import os
from platform import system as platform_system
import test_baseexception

def test_raise_string():
    UsageTests.raise_fails('spam')

UsageTests = test_baseexception.UsageTests()
test_raise_string()
