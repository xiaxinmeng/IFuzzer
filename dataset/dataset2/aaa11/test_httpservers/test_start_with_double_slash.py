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

def test_start_with_double_slash():
    path = SimpleHTTPRequestHandlerTestCase.handler_1.translate_path('//filename')
    SimpleHTTPRequestHandlerTestCase.assertEqual(path, SimpleHTTPRequestHandlerTestCase.translated_1)
    path = SimpleHTTPRequestHandlerTestCase.handler_2.translate_path('//filename')
    SimpleHTTPRequestHandlerTestCase.assertEqual(path, SimpleHTTPRequestHandlerTestCase.translated_2)
    path = SimpleHTTPRequestHandlerTestCase.handler_3.translate_path('//filename')
    SimpleHTTPRequestHandlerTestCase.assertEqual(path, SimpleHTTPRequestHandlerTestCase.translated_3)
    path = SimpleHTTPRequestHandlerTestCase.handler_1.translate_path('//filename?foo=bar')
    SimpleHTTPRequestHandlerTestCase.assertEqual(path, SimpleHTTPRequestHandlerTestCase.translated_1)
    path = SimpleHTTPRequestHandlerTestCase.handler_2.translate_path('//filename?foo=bar')
    SimpleHTTPRequestHandlerTestCase.assertEqual(path, SimpleHTTPRequestHandlerTestCase.translated_2)
    path = SimpleHTTPRequestHandlerTestCase.handler_3.translate_path('//filename?foo=bar')
    SimpleHTTPRequestHandlerTestCase.assertEqual(path, SimpleHTTPRequestHandlerTestCase.translated_3)

SimpleHTTPRequestHandlerTestCase = test_httpservers.SimpleHTTPRequestHandlerTestCase()
SimpleHTTPRequestHandlerTestCase.setUp()
test_start_with_double_slash()
