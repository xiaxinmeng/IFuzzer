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

def test_basic():
    NetworkTestCase.assertFalse(NetworkTestCase.parser.disallow_all)
    NetworkTestCase.assertFalse(NetworkTestCase.parser.allow_all)
    NetworkTestCase.assertGreater(NetworkTestCase.parser.mtime(), 0)
    NetworkTestCase.assertFalse(NetworkTestCase.parser.crawl_delay('*'))
    NetworkTestCase.assertFalse(NetworkTestCase.parser.request_rate('*'))

NetworkTestCase = test_robotparser.NetworkTestCase()
NetworkTestCase.setUp()
test_basic()
