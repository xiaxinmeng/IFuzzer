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

def test_header_buffering_of_send_header():
    input = BytesIO(b'GET / HTTP/1.1\r\n\r\n')
    output = test_httpservers.AuditableBytesIO()
    handler = test_httpservers.SocketlessRequestHandler()
    handler.rfile = input
    handler.wfile = output
    handler.request_version = 'HTTP/1.1'
    handler.send_header('Foo', 'foo')
    handler.send_header('bar', 'bar')
    BaseHTTPRequestHandlerTestCase.assertEqual(output.numWrites, 0)
    handler.end_headers()
    BaseHTTPRequestHandlerTestCase.assertEqual(output.getData(), b'Foo: foo\r\nbar: bar\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(output.numWrites, 1)

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_header_buffering_of_send_header()
