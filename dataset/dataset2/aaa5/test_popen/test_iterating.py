import unittest
from test import support
import os, sys
import test_popen

def test_iterating():
    with os.popen('echo hello') as f:
        PopenTest.assertEqual(list(f), ['hello\n'])

PopenTest = test_popen.PopenTest()
test_iterating()
