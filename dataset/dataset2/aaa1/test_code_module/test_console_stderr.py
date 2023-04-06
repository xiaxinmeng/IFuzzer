import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_console_stderr():
    TestInteractiveConsole.infunc.side_effect = ["'antioch'", '', EOFError('Finished')]
    TestInteractiveConsole.console.interact()
    for call in list(TestInteractiveConsole.stdout.method_calls):
        if 'antioch' in ''.join(call[1]):
            break
    else:
        raise AssertionError('no console stdout')

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_console_stderr()
