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

def test_read_404():
    parser = urllib.robotparser.RobotFileParser(NetworkTestCase.url('i-robot.txt'))
    parser.read()
    NetworkTestCase.assertTrue(parser.allow_all)
    NetworkTestCase.assertFalse(parser.disallow_all)
    NetworkTestCase.assertEqual(parser.mtime(), 0)
    NetworkTestCase.assertIsNone(parser.crawl_delay('*'))
    NetworkTestCase.assertIsNone(parser.request_rate('*'))

NetworkTestCase = test_robotparser.NetworkTestCase()
test_read_404()
