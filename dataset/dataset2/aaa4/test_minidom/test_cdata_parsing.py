import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_cdata_parsing():
    xml_str = '<?xml version="1.0" ?><root><node><![CDATA[</data>]]></node></root>'
    dom1 = parseString(xml_str)
    MinidomTest.checkWholeText(dom1.getElementsByTagName('node')[0].firstChild, '</data>')
    dom2 = parseString(dom1.toprettyxml())
    MinidomTest.checkWholeText(dom2.getElementsByTagName('node')[0].firstChild, '</data>')

MinidomTest = test_minidom.MinidomTest()
test_cdata_parsing()
