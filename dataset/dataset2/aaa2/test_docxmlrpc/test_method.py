from xmlrpc.server import DocXMLRPCServer
import http.client
import re
import sys
import threading
import unittest
import test_docxmlrpc

def test_method(TestClass, arg):
    """Test method's docs. This method truly does very little."""
    TestClass.arg = arg

TestClass = test_docxmlrpc.TestClass()
TestClass.setUp()
test_method()
