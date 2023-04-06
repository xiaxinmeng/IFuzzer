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

def test_html_escape_on_error():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'<script>alert("hello")</script> / HTTP/1.1')
    result = b''.join(result)
    text = '<script>alert("hello")</script>'
    BaseHTTPRequestHandlerTestCase.assertIn(html.escape(text, quote=False).encode('ascii'), result)

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_html_escape_on_error()
