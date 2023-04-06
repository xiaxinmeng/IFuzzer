import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_field_storage_multipart_no_content_length():
    fp = BytesIO(b'--MyBoundary\nContent-Disposition: form-data; name="my-arg"; filename="foo"\n\nTest\n\n--MyBoundary--\n')
    env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart/form-data; boundary=MyBoundary', 'wsgi.input': fp}
    fields = cgi.FieldStorage(fp, environ=env)
    CgiTests.assertEqual(len(fields['my-arg'].file.read()), 5)

CgiTests = test_cgi.CgiTests()
test_field_storage_multipart_no_content_length()
