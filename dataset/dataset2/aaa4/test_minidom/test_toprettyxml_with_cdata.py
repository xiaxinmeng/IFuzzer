import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_toprettyxml_with_cdata():
    xml_str = '<?xml version="1.0" ?><root><node><![CDATA[</data>]]></node></root>'
    doc = parseString(xml_str)
    MinidomTest.assertEqual(doc.toprettyxml(), '<?xml version="1.0" ?>\n<root>\n\t<node><![CDATA[</data>]]></node>\n</root>\n')

MinidomTest = test_minidom.MinidomTest()
test_toprettyxml_with_cdata()
