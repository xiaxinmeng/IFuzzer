from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

@test_docxmlrpc.make_request_and_skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_autolinking():
    """Test that the server correctly automatically wraps references to
        PEPS and RFCs with links, and that it linkifies text starting with
        http or ftp protocol prefixes.

        The documentation for the "add" method contains the test material.
        """
    DocXMLRPCHTTPGETServer.client.request('GET', '/')
    response = DocXMLRPCHTTPGETServer.client.getresponse().read()
    DocXMLRPCHTTPGETServer.assertIn(b'<dl><dt><a name="-add"><strong>add</strong></a>(x, y)</dt><dd><tt>Add&nbsp;two&nbsp;instances&nbsp;together.&nbsp;This&nbsp;follows&nbsp;<a href="http://www.python.org/dev/peps/pep-0008/">PEP008</a>,&nbsp;but&nbsp;has&nbsp;nothing<br>\nto&nbsp;do&nbsp;with&nbsp;<a href="http://www.rfc-editor.org/rfc/rfc1952.txt">RFC1952</a>.&nbsp;Case&nbsp;should&nbsp;matter:&nbsp;pEp008&nbsp;and&nbsp;rFC1952.&nbsp;&nbsp;Things<br>\nthat&nbsp;start&nbsp;with&nbsp;http&nbsp;and&nbsp;ftp&nbsp;should&nbsp;be&nbsp;auto-linked,&nbsp;too:<br>\n<a href="http://google.com">http://google.com</a>.</tt></dd></dl>', response)

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_autolinking()
