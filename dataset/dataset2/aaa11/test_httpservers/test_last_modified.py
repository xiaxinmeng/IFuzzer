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

def test_last_modified():
    """Checks that the datetime returned in Last-Modified response header
        is the actual datetime of last modification, rounded to the second
        """
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.base_url + '/test')
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.OK, data=SimpleHTTPServerTestCase.data)
    last_modif_header = response.headers['Last-modified']
    SimpleHTTPServerTestCase.assertEqual(last_modif_header, SimpleHTTPServerTestCase.last_modif_header)

SimpleHTTPServerTestCase = test_httpservers.SimpleHTTPServerTestCase()
SimpleHTTPServerTestCase.setUp()
test_last_modified()
