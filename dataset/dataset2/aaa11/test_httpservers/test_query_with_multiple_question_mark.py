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

def test_query_with_multiple_question_mark():
    res = CGIHTTPServerTestCase.request('/cgi-bin/file4.py?a=b?c=d')
    CGIHTTPServerTestCase.assertEqual((b'a=b?c=d' + CGIHTTPServerTestCase.linesep, 'text/html', HTTPStatus.OK), (res.read(), res.getheader('Content-type'), res.status))

CGIHTTPServerTestCase = test_httpservers.CGIHTTPServerTestCase()
CGIHTTPServerTestCase.setUp()
test_query_with_multiple_question_mark()
