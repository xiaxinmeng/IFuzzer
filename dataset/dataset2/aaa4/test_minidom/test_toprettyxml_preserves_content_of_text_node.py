import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_toprettyxml_preserves_content_of_text_node():
    for str in ('<B>A</B>', '<A><B>C</B></A>'):
        dom = parseString(str)
        dom2 = parseString(dom.toprettyxml())
        MinidomTest.assertEqual(dom.getElementsByTagName('B')[0].childNodes[0].toxml(), dom2.getElementsByTagName('B')[0].childNodes[0].toxml())

MinidomTest = test_minidom.MinidomTest()
test_toprettyxml_preserves_content_of_text_node()
