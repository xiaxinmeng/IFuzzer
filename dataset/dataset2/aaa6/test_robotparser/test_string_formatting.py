import io
import os
import threading
import unittest
import urllib.robotparser
from test import support
from test.support import socket_helper
from test.support import threading_helper
from http.server import BaseHTTPRequestHandler, HTTPServer
import test_robotparser

def test_string_formatting():
    StringFormattingTest.assertEqual(str(StringFormattingTest.parser), StringFormattingTest.expected_output)

StringFormattingTest = test_robotparser.StringFormattingTest()
StringFormattingTest.setUp()
test_string_formatting()
