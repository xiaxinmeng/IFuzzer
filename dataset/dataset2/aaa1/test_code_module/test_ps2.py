import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_ps2():
    TestInteractiveConsole.infunc.side_effect = EOFError('Finished')
    TestInteractiveConsole.console.interact()
    TestInteractiveConsole.assertEqual(TestInteractiveConsole.sysmod.ps2, '... ')
    TestInteractiveConsole.sysmod.ps1 = 'custom2> '
    TestInteractiveConsole.console.interact()
    TestInteractiveConsole.assertEqual(TestInteractiveConsole.sysmod.ps1, 'custom2> ')

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_ps2()
