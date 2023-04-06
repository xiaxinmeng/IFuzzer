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

@mock.patch('builtins.print')
def test_server_test_localhost(ScriptTestCase, _):
    mock_server = ScriptTestCase.mock_server_class()
    server.test(ServerClass=mock_server, bind='localhost')
    ScriptTestCase.assertIn(mock_server.address_family, (socket.AF_INET6, socket.AF_INET))

ScriptTestCase = test_httpservers.ScriptTestCase()
test_server_test_localhost()
