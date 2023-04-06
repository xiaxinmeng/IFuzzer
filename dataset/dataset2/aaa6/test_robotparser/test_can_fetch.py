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

def test_can_fetch():
    NetworkTestCase.assertTrue(NetworkTestCase.parser.can_fetch('*', NetworkTestCase.url('elsewhere')))
    NetworkTestCase.assertFalse(NetworkTestCase.parser.can_fetch('Nutch', NetworkTestCase.base_url))
    NetworkTestCase.assertFalse(NetworkTestCase.parser.can_fetch('Nutch', NetworkTestCase.url('brian')))
    NetworkTestCase.assertFalse(NetworkTestCase.parser.can_fetch('Nutch', NetworkTestCase.url('webstats')))
    NetworkTestCase.assertFalse(NetworkTestCase.parser.can_fetch('*', NetworkTestCase.url('webstats')))
    NetworkTestCase.assertTrue(NetworkTestCase.parser.can_fetch('*', NetworkTestCase.base_url))

NetworkTestCase = test_robotparser.NetworkTestCase()
test_can_fetch()
