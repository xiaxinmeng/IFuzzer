import unittest
import builtins
import os
from platform import system as platform_system
import test_baseexception

def test_raise_new_style_non_exception():

    class NewStyleClass(object):
        pass
    UsageTests.raise_fails(NewStyleClass)
    UsageTests.raise_fails(NewStyleClass())

UsageTests = test_baseexception.UsageTests()
test_raise_new_style_non_exception()
