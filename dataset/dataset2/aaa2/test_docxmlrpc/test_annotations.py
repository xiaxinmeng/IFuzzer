from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_annotations():
    """ Test that annotations works as expected """
    DocXMLRPCHTTPGETServer.client.request('GET', '/')
    response = DocXMLRPCHTTPGETServer.client.getresponse()
    docstring = b'' if sys.flags.optimize >= 2 else b'<dd><tt>Use&nbsp;function&nbsp;annotations.</tt></dd>'
    DocXMLRPCHTTPGETServer.assertIn(b'<dl><dt><a name="-annotation"><strong>annotation</strong></a>(x: int)</dt>' + docstring + b'</dl>\n<dl><dt><a name="-method_annotation"><strong>method_annotation</strong></a>(x: bytes)</dt></dl>', response.read())

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_annotations()
