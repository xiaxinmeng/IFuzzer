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

def test_site_maps():
    BaseRobotTest.assertEqual(BaseRobotTest.parser.site_maps(), BaseRobotTest.site_maps)

BaseRobotTest = test_robotparser.BaseRobotTest()
BaseRobotTest.setUp()
test_site_maps()
