from collections import OrderedDict
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler, CGIHTTPRequestHandler
from http import server, HTTPStatus
import os
import socket
import sys
import re
import base64
import ntpath
import pathlib
import shutil
import email.message
import email.utils
import html
import http, http.client
import urllib.parse
import tempfile
import time
import datetime
import threading
from unittest import mock
from io import BytesIO
import unittest
from test import support
from test.support import os_helper
from test.support import threading_helper
import test_httpservers

def test_with_continue_rejected():
    usual_handler = BaseHTTPRequestHandlerTestCase.handler
    BaseHTTPRequestHandlerTestCase.handler = test_httpservers.RejectingSocketlessRequestHandler()
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET / HTTP/1.1\r\nExpect: 100-continue\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(result[0], b'HTTP/1.1 417 Expectation Failed\r\n')
    BaseHTTPRequestHandlerTestCase.verify_expected_headers(result[1:-1])
    BaseHTTPRequestHandlerTestCase.assertFalse(BaseHTTPRequestHandlerTestCase.handler.get_called)
    BaseHTTPRequestHandlerTestCase.assertEqual(sum((r == b'Connection: close\r\n' for r in result[1:-1])), 1)
    BaseHTTPRequestHandlerTestCase.handler = usual_handler

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_with_continue_rejected()
