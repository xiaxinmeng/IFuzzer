import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_toprettyxml_with_adjacent_text_nodes():
    dom = Document()
    elem = dom.createElement('elem')
    elem.appendChild(dom.createTextNode('TEXT'))
    elem.appendChild(dom.createTextNode('TEXT'))
    dom.appendChild(elem)
    decl = '<?xml version="1.0" ?>\n'
    MinidomTest.assertEqual(dom.toprettyxml(), decl + '<elem>\n\tTEXT\n\tTEXT\n</elem>\n')

MinidomTest = test_minidom.MinidomTest()
test_toprettyxml_with_adjacent_text_nodes()
