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

def test_version_invalid():
    BaseHTTPServerTestCase.con._http_vsn = 99
    BaseHTTPServerTestCase.con._http_vsn_str = 'HTTP/9.9'
    BaseHTTPServerTestCase.con.putrequest('GET', '/')
    BaseHTTPServerTestCase.con.endheaders()
    res = BaseHTTPServerTestCase.con.getresponse()
    BaseHTTPServerTestCase.assertEqual(res.status, HTTPStatus.HTTP_VERSION_NOT_SUPPORTED)

BaseHTTPServerTestCase = test_httpservers.BaseHTTPServerTestCase()
BaseHTTPServerTestCase.setUp()
test_version_invalid()
