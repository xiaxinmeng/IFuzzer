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

def test_extra_space():
    result = BaseHTTPRequestHandlerTestCase.send_typical_request(b'GET /spaced out HTTP/1.1\r\nHost: dummy\r\n\r\n')
    BaseHTTPRequestHandlerTestCase.assertTrue(result[0].startswith(b'HTTP/1.1 400 '))
    BaseHTTPRequestHandlerTestCase.verify_expected_headers(result[1:result.index(b'\r\n')])
    BaseHTTPRequestHandlerTestCase.assertFalse(BaseHTTPRequestHandlerTestCase.handler.get_called)

BaseHTTPRequestHandlerTestCase = test_httpservers.BaseHTTPRequestHandlerTestCase()
BaseHTTPRequestHandlerTestCase.setUp()
test_extra_space()
