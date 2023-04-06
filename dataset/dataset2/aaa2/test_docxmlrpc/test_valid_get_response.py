from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_valid_get_response():
    DocXMLRPCHTTPGETServer.client.request('GET', '/')
    response = DocXMLRPCHTTPGETServer.client.getresponse()
    DocXMLRPCHTTPGETServer.assertEqual(response.status, 200)
    DocXMLRPCHTTPGETServer.assertEqual(response.getheader('Content-type'), 'text/html')
    response.read()

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_valid_get_response()
