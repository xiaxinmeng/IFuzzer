from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_invalid_get_response():
    DocXMLRPCHTTPGETServer.client.request('GET', '/spam')
    response = DocXMLRPCHTTPGETServer.client.getresponse()
    DocXMLRPCHTTPGETServer.assertEqual(response.status, 404)
    DocXMLRPCHTTPGETServer.assertEqual(response.getheader('Content-type'), 'text/plain')
    response.read()

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_invalid_get_response()
