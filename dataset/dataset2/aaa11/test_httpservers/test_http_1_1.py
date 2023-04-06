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

def test_http_1_1():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET / HTTP/1.1\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.verify_http_server_response(result[0])
    BaseHTTPRequestHandlerTestCase.verify_expected_headers(result[1:-1])
    BaseHTTPRequestHandlerTestCase.verify_get_called()
    BaseHTTPRequestHandlerTestCase.assertEqual(result[-1], b'<html><body>Data</body></html>\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.requestline, 'GET / HTTP/1.1')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.command, 'GET')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.path, '/')
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.request_version, 'HTTP/1.1')
    BaseHTTPRequestHandlerTestCase.assertSequenceEqual(BaseHTTPRequestHandlerTestCase.handler.headers.items(), ())

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_http_1_1()
