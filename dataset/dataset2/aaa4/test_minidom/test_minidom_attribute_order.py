import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_minidom_attribute_order():
    xml_str = '<?xml version="1.0" ?><curriculum status="public" company="example"/>'
    doc = parseString(xml_str)
    output = io.StringIO()
    doc.writexml(output)
    MinidomTest.assertEqual(output.getvalue(), xml_str)

MinidomTest = test_minidom.MinidomTest()
test_minidom_attribute_order()
