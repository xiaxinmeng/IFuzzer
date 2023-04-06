import copy
import pickle
import io
from test import support
import unittest
import xml.dom.minidom
from xml.dom.minidom import parse, Node, Document, parseString
from xml.dom.minidom import getDOMImplementation
import test_minidom

def test_toprettyxml_with_text_nodes():
    decl = '<?xml version="1.0" ?>\n'
    MinidomTest.assertEqual(parseString('<B>A</B>').toprettyxml(), decl + '<B>A</B>\n')
    MinidomTest.assertEqual(parseString('<C>A<B>A</B></C>').toprettyxml(), decl + '<C>\n\tA\n\t<B>A</B>\n</C>\n')
    MinidomTest.assertEqual(parseString('<C><B>A</B>A</C>').toprettyxml(), decl + '<C>\n\t<B>A</B>\n\tA\n</C>\n')
    MinidomTest.assertEqual(parseString('<C><B>A</B><B>A</B></C>').toprettyxml(), decl + '<C>\n\t<B>A</B>\n\t<B>A</B>\n</C>\n')
    MinidomTest.assertEqual(parseString('<C><B>A</B>A<B>A</B></C>').toprettyxml(), decl + '<C>\n\t<B>A</B>\n\tA\n\t<B>A</B>\n</C>\n')

MinidomTest = test_minidom.MinidomTest()
test_toprettyxml_with_text_nodes()
