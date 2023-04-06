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

def test_http_0_9():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET / HTTP/0.9\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.assertEqual(len(result), 1)
    BaseHTTPRequestHandlerTestCase.assertEqual(result[0], b'<html><body>Data</body></html>\r\n')
    BaseHTTPRequestHandlerTestCase.verify_get_called()

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_http_0_9()
