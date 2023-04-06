import unittest
from test import support
import os, sys
import test_popen

def test_keywords():
    with os.popen(cmd='exit 0', mode='w', buffering=-1):
        pass

PopenTest = test_popen.PopenTest()
test_keywords()
