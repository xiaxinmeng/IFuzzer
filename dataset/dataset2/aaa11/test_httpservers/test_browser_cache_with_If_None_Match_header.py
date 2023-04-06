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

def test_browser_cache_with_If_None_Match_header():
    headers = email.message.Message()
    headers['If-Modified-Since'] = SimpleHTTPServerTestCase.last_modif_header
    headers['If-None-Match'] = '*'
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.base_url + '/test', headers=headers)
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.OK)

SimpleHTTPServerTestCase = test_httpservers.SimpleHTTPServerTestCase()
SimpleHTTPServerTestCase.setUp()
test_browser_cache_with_If_None_Match_header()
