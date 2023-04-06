import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_fieldstorage_invalid():
    CgiTests.assertRaises(TypeError, cgi.FieldStorage, 'not-a-file-obj', environ={'REQUEST_METHOD': 'PUT'})
    CgiTests.assertRaises(TypeError, cgi.FieldStorage, 'foo', 'bar')
    fs = cgi.FieldStorage(headers={'content-type': 'text/plain'})
    CgiTests.assertRaises(TypeError, bool, fs)

CgiTests = test_cgi.CgiTests()
test_fieldstorage_invalid()
