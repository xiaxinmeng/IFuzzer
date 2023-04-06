from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_lambda():
    """Test that lambda functionality stays the same.  The output produced
        currently is, I suspect invalid because of the unencoded brackets in the
        HTML, "<lambda>".

        The subtraction lambda method is tested.
        """
    DocXMLRPCHTTPGETServer.client.request('GET', '/')
    response = DocXMLRPCHTTPGETServer.client.getresponse()
    DocXMLRPCHTTPGETServer.assertIn(b'<dl><dt><a name="-&lt;lambda&gt;"><strong>&lt;lambda&gt;</strong></a>(x, y)</dt></dl>', response.read())

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_lambda()
