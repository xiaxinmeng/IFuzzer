import cmd
import sys
import unittest
import io
from test import support
from test import test_cmd
import test_cmd

def test_file_with_missing_final_nl():
    input = io.StringIO('print test\nprint test2')
    output = io.StringIO()
    cmd = TestAlternateInput.simplecmd(stdin=input, stdout=output)
    cmd.use_rawinput = False
    cmd.cmdloop()
    TestAlternateInput.assertMultiLineEqual(output.getvalue(), '(Cmd) test\n(Cmd) test2\n(Cmd) ')

TestAlternateInput = test_cmd.TestAlternateInput()
test_file_with_missing_final_nl()
