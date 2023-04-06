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

def test_parse_only_xml_data():
    xml = "<?xml version='1.0' encoding='iso8859'?><s>%s</s>" % ('a' * 1025)

    class SpecificException(Exception):
        pass

    def handler(text):
        raise SpecificException
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = handler
    sf1296433Test.assertRaises(Exception, parser.Parse, xml.encode('iso8859'))

sf1296433Test = test_pyexpat.sf1296433Test()
test_parse_only_xml_data()
