import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_sysexcepthook():
    TestInteractiveConsole.infunc.side_effect = ["raise ValueError('')", EOFError('Finished')]
    hook = mock.Mock()
    TestInteractiveConsole.sysmod.excepthook = hook
    TestInteractiveConsole.console.interact()
    TestInteractiveConsole.assertTrue(hook.called)

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_sysexcepthook()
