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

def test_send_blank():
    BaseHTTPServerTestCase.con._http_vsn_str = ''
    BaseHTTPServerTestCase.con.putrequest('', '')
    BaseHTTPServerTestCase.con.endheaders()
    res = BaseHTTPServerTestCase.con.getresponse()
    BaseHTTPServerTestCase.assertEqual(res.status, HTTPStatus.BAD_REQUEST)

BaseHTTPServerTestCase = test_httpservers.BaseHTTPServerTestCase()
BaseHTTPServerTestCase.setUp()
test_send_blank()
