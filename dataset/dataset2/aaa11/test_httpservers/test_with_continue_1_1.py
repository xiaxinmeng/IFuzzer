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

def test_with_continue_1_1():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET / HTTP/1.1\r\nExpect: 100-continue\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(result[0], b'HTTP/1.1 100 Continue\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(result[1], b'\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(result[2], b'HTTP/1.1 200 OK\r\n')
    BaseHTTPRequestHandlerTestCase.verify_expected_headers(result[2:-1])
    BaseHTTPRequestHandlerTestCase.verify_get_called()
    BaseHTTPRequestHandlerTestCase.assertEqual(result[-1], b'<html><body>Data</body></html>\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.requestline, 'GET / HTTP/1.1')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.command, 'GET')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.path, '/')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.request_version, 'HTTP/1.1')
    headers = (('Expect', '100-continue'),)
    BaseHTTPRequestHandlerTestCase.assertSequenceEqual(BaseHTTPRequestHandlerTestCase.handler.headers.items(), headers)

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_with_continue_1_1()
