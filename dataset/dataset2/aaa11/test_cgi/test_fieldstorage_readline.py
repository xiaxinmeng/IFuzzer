import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_fieldstorage_readline():

    class TestReadlineFile:

        def __init__(CgiTests, file):
            CgiTests.file = file
            CgiTests.numcalls = 0

        def readline(CgiTests, size=None):
            CgiTests.numcalls += 1
            if size:
                return CgiTests.file.readline(size)
            else:
                return CgiTests.file.readline()

        def __getattr__(CgiTests, name):
            file = CgiTests.__dict__['file']
            a = getattr(file, name)
            if not isinstance(a, int):
                setattr(CgiTests, name, a)
            return a
    f = TestReadlineFile(tempfile.TemporaryFile('wb+'))
    CgiTests.addCleanup(f.close)
    f.write(b'x' * 256 * 1024)
    f.seek(0)
    env = {'REQUEST_METHOD': 'PUT'}
    fs = cgi.FieldStorage(fp=f, environ=env)
    CgiTests.addCleanup(fs.file.close)
    CgiTests.assertGreater(f.numcalls, 2)
    f.close()

CgiTests = test_cgi.CgiTests()
test_fieldstorage_readline()
