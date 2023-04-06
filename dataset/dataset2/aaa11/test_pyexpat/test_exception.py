from io import BytesIO
import os
import platform
import sys
import sysconfig
import unittest
import traceback
from xml.parsers import expat
from xml.parsers.expat import errors
from test.support import sortdict
import test_pyexpat

def test_exception():
    parser = expat.ParserCreate()
    parser.StartElementHandler = HandlerExceptionTest.StartElementHandler
    try:
        parser.Parse(b'<a><b><c/></b></a>', True)
        HandlerExceptionTest.fail()
    except RuntimeError as e:
        HandlerExceptionTest.assertEqual(e.args[0], 'a', "Expected RuntimeError for element 'a', but" + ' found %r' % e.args[0])
        entries = traceback.extract_tb(e.__traceback__)
        HandlerExceptionTest.assertEqual(len(entries), 3)
        HandlerExceptionTest.check_traceback_entry(entries[0], 'test_pyexpat.py', 'test_exception')
        HandlerExceptionTest.check_traceback_entry(entries[1], 'pyexpat.c', 'StartElement')
        HandlerExceptionTest.check_traceback_entry(entries[2], 'test_pyexpat.py', 'StartElementHandler')
        if sysconfig.is_python_build() and (not (sys.platform == 'win32' and platform.machine() == 'ARM')):
            HandlerExceptionTest.assertIn('call_with_frame("StartElement"', entries[1][3])

HandlerExceptionTest = test_pyexpat.HandlerExceptionTest()
test_exception()
