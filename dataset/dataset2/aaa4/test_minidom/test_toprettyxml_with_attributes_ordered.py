import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_toprettyxml_with_attributes_ordered():
    xml_str = '<?xml version="1.0" ?><curriculum status="public" company="example"/>'
    doc = parseString(xml_str)
    MinidomTest.assertEqual(doc.toprettyxml(), '<?xml version="1.0" ?>\n<curriculum status="public" company="example"/>\n')

MinidomTest = test_minidom.MinidomTest()
test_toprettyxml_with_attributes_ordered()
