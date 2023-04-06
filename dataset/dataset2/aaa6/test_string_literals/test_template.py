import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_template():
    for c in test_string_literals.TEMPLATE:
        assert c == '\n' or ' ' <= c <= '~', repr(c)

TestLiterals = test_string_literals.TestLiterals()
test_template()
