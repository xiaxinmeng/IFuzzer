import unittest
from test import support
import os, sys
import test_popen

def test_contextmanager():
    with os.popen('echo hello') as f:
        PopenTest.assertEqual(f.read(), 'hello\n')

PopenTest = test_popen.PopenTest()
test_contextmanager()
