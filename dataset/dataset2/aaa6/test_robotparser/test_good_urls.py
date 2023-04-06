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

def test_good_urls():
    for url in BaseRobotTest.good:
        (agent, url) = BaseRobotTest.get_agent_and_url(url)
        with BaseRobotTest.subTest(url=url, agent=agent):
            BaseRobotTest.assertTrue(BaseRobotTest.parser.can_fetch(agent, url))

BaseRobotTest = test_robotparser.BaseRobotTest()
test_good_urls()
