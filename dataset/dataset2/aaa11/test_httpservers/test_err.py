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

def test_err():
    RequestHandlerLoggingTestCase.con = http.client.HTTPConnection(RequestHandlerLoggingTestCase.HOST, RequestHandlerLoggingTestCase.PORT)
    RequestHandlerLoggingTestCase.con.connect()
    with support.captured_stderr() as err:
        RequestHandlerLoggingTestCase.con.request('ERROR', '/')
        RequestHandlerLoggingTestCase.con.getresponse()
    lines = err.getvalue().split('\n')
    RequestHandlerLoggingTestCase.assertTrue(lines[0].endswith('code 404, message File not found'))
    RequestHandlerLoggingTestCase.assertTrue(lines[1].endswith('"ERROR / HTTP/1.1" 404 -'))

RequestHandlerLoggingTestCase = test_httpservers.RequestHandlerLoggingTestCase()
RequestHandlerLoggingTestCase.setUp() 
test_err()
