from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_server_title_escape():
    DocXMLRPCHTTPGETServer.serv.set_server_title('test_title<script>')
    DocXMLRPCHTTPGETServer.serv.set_server_documentation('test_documentation<script>')
    DocXMLRPCHTTPGETServer.assertEqual('test_title<script>', DocXMLRPCHTTPGETServer.serv.server_title)
    DocXMLRPCHTTPGETServer.assertEqual('test_documentation<script>', DocXMLRPCHTTPGETServer.serv.server_documentation)
    generated = DocXMLRPCHTTPGETServer.serv.generate_html_documentation()
    title = re.search('<title>(.+?)</title>', generated).group()
    documentation = re.search('<p><tt>(.+?)</tt></p>', generated).group()
    DocXMLRPCHTTPGETServer.assertEqual('<title>Python: test_title&lt;script&gt;</title>', title)
    DocXMLRPCHTTPGETServer.assertEqual('<p><tt>test_documentation&lt;script&gt;</tt></p>', documentation)

DocXMLRPCHTTPGETServer = test_docxmlrpc.DocXMLRPCHTTPGETServer()
DocXMLRPCHTTPGETServer.setUp()
test_server_title_escape()
