from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

@test_docxmlrpc.make_request_and_skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_system_methods():
    """Test the presence of three consecutive system.* methods.

        This also tests their use of parameter type recognition and the
        systems related to that process.
        """
    DocXMLRPCHTTPGETServer.client.request('GET', '/')
    response = DocXMLRPCHTTPGETServer.client.getresponse().read()
    DocXMLRPCHTTPGETServer.assertIn(b'<dl><dt><a name="-system.methodHelp"><strong>system.methodHelp</strong></a>(method_name)</dt><dd><tt><a href="#-system.methodHelp">system.methodHelp</a>(\'add\')&nbsp;=&gt;&nbsp;"Adds&nbsp;two&nbsp;integers&nbsp;together"<br>\n&nbsp;<br>\nReturns&nbsp;a&nbsp;string&nbsp;containing&nbsp;documentation&nbsp;for&nbsp;the&nbsp;specified&nbsp;method.</tt></dd></dl>\n<dl><dt><a name="-system.methodSignature"><strong>system.methodSignature</strong></a>(method_name)</dt><dd><tt><a href="#-system.methodSignature">system.methodSignature</a>(\'add\')&nbsp;=&gt;&nbsp;[double,&nbsp;int,&nbsp;int]<br>\n&nbsp;<br>\nReturns&nbsp;a&nbsp;list&nbsp;describing&nbsp;the&nbsp;signature&nbsp;of&nbsp;the&nbsp;method.&nbsp;In&nbsp;the<br>\nabove&nbsp;example,&nbsp;the&nbsp;add&nbsp;method&nbsp;takes&nbsp;two&nbsp;integers&nbsp;as&nbsp;arguments<br>\nand&nbsp;returns&nbsp;a&nbsp;double&nbsp;result.<br>\n&nbsp;<br>\nThis&nbsp;server&nbsp;does&nbsp;NOT&nbsp;support&nbsp;system.methodSignature.</tt></dd></dl>', response)

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_system_methods()
