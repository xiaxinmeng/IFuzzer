import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_parse_multipart():
    fp = BytesIO(test_cgi.POSTDATA.encode('latin1'))
    env = {'boundary': test_cgi.BOUNDARY.encode('latin1'), 'CONTENT-LENGTH': '558'}
    result = cgi.parse_multipart(fp, env)
    expected = {'submit': [' Add '], 'id': ['1234'], 'file': [b'Testing 123.\n'], 'title': ['']}
    CgiTests.assertEqual(result, expected)

CgiTests = test_cgi.CgiTests()
test_parse_multipart()
