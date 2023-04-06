import mailcap
import os
import copy
import test.support
from test.support import os_helper
import unittest
import sys
import test_mailcap

def test_subst():
    plist = ['id=1', 'number=2', 'total=3']
    test_cases = [(['', 'audio/*', 'foo.txt'], ''), (['echo foo', 'audio/*', 'foo.txt'], 'echo foo'), (['echo %s', 'audio/*', 'foo.txt'], 'echo foo.txt'), (['echo %t', 'audio/*', 'foo.txt'], 'echo audio/*'), (['echo \\%t', 'audio/*', 'foo.txt'], 'echo %t'), (['echo foo', 'audio/*', 'foo.txt', plist], 'echo foo'), (['echo %{total}', 'audio/*', 'foo.txt', plist], 'echo 3')]
    for tc in test_cases:
        HelperFunctionTest.assertEqual(mailcap.subst(*tc[0]), tc[1])

HelperFunctionTest = test_mailcap.HelperFunctionTest()
test_subst()
