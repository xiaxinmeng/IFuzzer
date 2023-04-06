from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_autolink_dotted_methods():
    """Test that DocXMLRPCHTTPGETServerdot values are made strong automatically in the
        documentation."""
    DocXMLRPCHTTPGETServer.client.request('GET', '/')
    response = DocXMLRPCHTTPGETServer.client.getresponse()
    DocXMLRPCHTTPGETServer.assertIn(b'Try&nbsp;DocXMLRPCHTTPGETServer.<strong>add</strong>,&nbsp;too.', response.read())

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_autolink_dotted_methods()
