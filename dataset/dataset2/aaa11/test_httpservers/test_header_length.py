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

def test_header_length():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET / HTTP/1.1\r\nX-Foo: bar' + b'r' * 65537 + b'\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(result[0], b'HTTP/1.1 431 Line too long\r\n')
    BaseHTTPRequestHandlerTestCase.assertFalse(BaseHTTPRequestHandlerTestCase.handler.get_called)
    BaseHTTPRequestHandlerTestCase.assertEqual(BaseHTTPRequestHandlerTestCase.handler.requestline, 'GET / HTTP/1.1')

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_header_length()
