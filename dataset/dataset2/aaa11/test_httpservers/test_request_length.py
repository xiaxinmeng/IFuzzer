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

def test_request_length():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET ' + b'x' * 65537)
    BaseHTTPRequestHandlerTestCase.assertEqual(result[0], b'HTTP/1.1 414 Request-URI Too Long\r\n')
    BaseHTTPRequestHandlerTestCase.assertFalse(BaseHTTPRequestHandlerTestCase.handler.get_called)
    BaseHTTPRequestHandlerTestCase.assertIsInstance(BaseHTTPRequestHandlerTestCase.handler.requestline, str)

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_request_length()
