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

def test_parse_file():
    out = ParseTest.Outputter()
    parser = expat.ParserCreate(namespace_separator='!')
    ParseTest._hookup_callbacks(parser, out)
    file = BytesIO(test_pyexpat.data)
    parser.ParseFile(file)
    operations = out.out
    ParseTest._verify_parse_output(operations)

ParseTest = test_pyexpat.ParseTest()
test_parse_file()
