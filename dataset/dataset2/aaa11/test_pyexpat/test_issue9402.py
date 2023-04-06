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

def test_issue9402():

    class ExternalOutputter:

        def __init__(InterningTest, parser):
            InterningTest.parser = parser
            InterningTest.parser_result = None

        def ExternalEntityRefHandler(InterningTest, context, base, sysId, pubId):
            external_parser = InterningTest.parser.ExternalEntityParserCreate('')
            InterningTest.parser_result = external_parser.Parse(b'', True)
            return 1
    parser = expat.ParserCreate(namespace_separator='!')
    parser.buffer_text = 1
    out = ExternalOutputter(parser)
    parser.ExternalEntityRefHandler = out.ExternalEntityRefHandler
    parser.Parse(test_pyexpat.data, True)
    InterningTest.assertEqual(out.parser_result, 1)

InterningTest = test_pyexpat.InterningTest()
test_issue9402()
