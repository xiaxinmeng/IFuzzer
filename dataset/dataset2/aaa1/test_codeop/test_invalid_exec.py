import sys
import unittest
import warnings
from test import support
from test.support import warnings_helper
from codeop import compile_command, PyCF_DONT_IMPLY_DEDENT
import io
import test_codeop

def test_invalid_exec():
    ai = CodeopTests.assertInvalid
    ai('raise = 4', symbol='exec')
    ai('def a-b', symbol='exec')
    ai('await?', symbol='exec')
    ai('=!=', symbol='exec')
    ai('a await raise b', symbol='exec')
    ai('a await raise b?+1', symbol='exec')

CodeopTests = test_codeop.CodeopTests()
test_invalid_exec()
