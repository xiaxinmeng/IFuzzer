import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_parse_header():
    CgiTests.assertEqual(cgi.parse_header('text/plain'), ('text/plain', {}))
    CgiTests.assertEqual(cgi.parse_header('text/vnd.just.made.this.up ; '), ('text/vnd.just.made.this.up', {}))
    CgiTests.assertEqual(cgi.parse_header('text/plain;charset=us-ascii'), ('text/plain', {'charset': 'us-ascii'}))
    CgiTests.assertEqual(cgi.parse_header('text/plain ; charset="us-ascii"'), ('text/plain', {'charset': 'us-ascii'}))
    CgiTests.assertEqual(cgi.parse_header('text/plain ; charset="us-ascii"; another=opt'), ('text/plain', {'charset': 'us-ascii', 'another': 'opt'}))
    CgiTests.assertEqual(cgi.parse_header('attachment; filename="silly.txt"'), ('attachment', {'filename': 'silly.txt'}))
    CgiTests.assertEqual(cgi.parse_header('attachment; filename="strange;name"'), ('attachment', {'filename': 'strange;name'}))
    CgiTests.assertEqual(cgi.parse_header('attachment; filename="strange;name";size=123;'), ('attachment', {'filename': 'strange;name', 'size': '123'}))
    CgiTests.assertEqual(cgi.parse_header('form-data; name="files"; filename="fo\\"o;bar"'), ('form-data', {'name': 'files', 'filename': 'fo"o;bar'}))

CgiTests = test_cgi.CgiTests()
test_parse_header()
