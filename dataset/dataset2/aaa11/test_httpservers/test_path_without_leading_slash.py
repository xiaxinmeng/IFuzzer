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

def test_path_without_leading_slash():
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.tempdir_name + '/test')
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.OK, data=SimpleHTTPServerTestCase.data)
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.tempdir_name + '/test/')
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.NOT_FOUND)
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.tempdir_name + '/')
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.OK)
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.tempdir_name)
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.tempdir_name + '/?hi=2')
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.OK)
    response = SimpleHTTPServerTestCase.request(SimpleHTTPServerTestCase.tempdir_name + '?hi=1')
    SimpleHTTPServerTestCase.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    SimpleHTTPServerTestCase.assertEqual(response.getheader('Location'), SimpleHTTPServerTestCase.tempdir_name + '/?hi=1')

SimpleHTTPServerTestCase = test_httpservers.SimpleHTTPServerTestCase()
SimpleHTTPServerTestCase.setUp()
test_path_without_leading_slash()
