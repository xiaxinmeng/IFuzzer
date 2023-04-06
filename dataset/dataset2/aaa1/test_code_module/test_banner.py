import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_banner():
    TestInteractiveConsole.infunc.side_effect = EOFError('Finished')
    TestInteractiveConsole.console.interact(banner='Foo')
    TestInteractiveConsole.assertEqual(len(TestInteractiveConsole.stderr.method_calls), 3)
    banner_call = TestInteractiveConsole.stderr.method_calls[0]
    TestInteractiveConsole.assertEqual(banner_call, ['write', ('Foo\n',), {}])
    TestInteractiveConsole.stderr.reset_mock()
    TestInteractiveConsole.infunc.side_effect = EOFError('Finished')
    TestInteractiveConsole.console.interact(banner='')
    TestInteractiveConsole.assertEqual(len(TestInteractiveConsole.stderr.method_calls), 2)

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_banner()
