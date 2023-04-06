import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_ps1():
    TestInteractiveConsole.infunc.side_effect = EOFError('Finished')
    TestInteractiveConsole.console.interact()
    TestInteractiveConsole.assertEqual(TestInteractiveConsole.sysmod.ps1, '>>> ')
    TestInteractiveConsole.sysmod.ps1 = 'custom1> '
    TestInteractiveConsole.console.interact()
    TestInteractiveConsole.assertEqual(TestInteractiveConsole.sysmod.ps1, 'custom1> ')

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_ps1()
