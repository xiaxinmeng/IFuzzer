import cmd
import sys
import unittest
import io
from test import support
from test import test_cmd
import test_cmd

def test_input_reset_at_EOF():
    input = io.StringIO('print test\nprint test2')
    output = io.StringIO()
    cmd = TestAlternateInput.simplecmd2(stdin=input, stdout=output)
    cmd.use_rawinput = False
    cmd.cmdloop()
    TestAlternateInput.assertMultiLineEqual(output.getvalue(), '(Cmd) test\n(Cmd) test2\n(Cmd) *** Unknown syntax: EOF\n')
    input = io.StringIO('print \n\n')
    output = io.StringIO()
    cmd.stdin = input
    cmd.stdout = output
    cmd.cmdloop()
    TestAlternateInput.assertMultiLineEqual(output.getvalue(), '(Cmd) \n(Cmd) \n(Cmd) *** Unknown syntax: EOF\n')

TestAlternateInput = test_cmd.TestAlternateInput()
test_input_reset_at_EOF()
