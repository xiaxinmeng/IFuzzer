import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_mixed_types_filenames():
    a = ['hello\n']
    b = ['ohell\n']
    fna = b'ol\xe9.txt'
    fnb = b'ol\xc3a9.txt'
    TestBytes._assert_type_error("all arguments must be str, not: b'ol\\xe9.txt'", difflib.unified_diff, a, b, fna, fnb)

TestBytes = test_difflib.TestBytes()
test_mixed_types_filenames()
