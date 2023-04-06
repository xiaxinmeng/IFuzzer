import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_all():
    not_exported = {'logfile', 'logfp', 'initlog', 'dolog', 'nolog', 'closelog', 'log', 'maxlen', 'valid_boundary'}
    support.check__all__(CgiTests, cgi, not_exported=not_exported)

CgiTests = test_cgi.CgiTests()
test_all()
