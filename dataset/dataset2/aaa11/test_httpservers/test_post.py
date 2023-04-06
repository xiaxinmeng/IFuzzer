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

def test_post():
    params = urllib.parse.urlencode({'spam': 1, 'eggs': 'python', 'bacon': 123456})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    res = CGIHTTPServerTestCase.request('/cgi-bin/file2.py', 'POST', params, headers)
    CGIHTTPServerTestCase.assertEqual(res.read(), b'1, python, 123456' + CGIHTTPServerTestCase.linesep)

CGIHTTPServerTestCase = test_httpservers.CGIHTTPServerTestCase()
CGIHTTPServerTestCase.setUp()
test_post()
