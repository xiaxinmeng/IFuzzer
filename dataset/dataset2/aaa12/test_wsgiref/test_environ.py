from unittest import mock
from test import support
from test.support import socket_helper
from test.support import warnings_helper
from test.test_httpservers import NoLogRequestHandler
from unittest import TestCase
from wsgiref.util import setup_testing_defaults
from wsgiref.headers import Headers
from wsgiref.handlers import BaseHandler, BaseCGIHandler, SimpleHandler
from wsgiref import util
from wsgiref.validate import validator
from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
from wsgiref.simple_server import make_server
from http.client import HTTPConnection
from io import StringIO, BytesIO, BufferedReader
from socketserver import BaseServer
from platform import python_implementation
import os
import re
import signal
import sys
import threading
import unittest
import test_wsgiref

def test_environ():
    request = b'GET /p%61th/?query=test HTTP/1.0\nX-Test-Header: Python test \nX-Test-Header: Python test 2\nContent-Length: 0\n\n'
    (out, err) = test_wsgiref.run_amock(test_wsgiref.header_app, request)
    IntegrationTests.assertEqual(out.splitlines()[-1], b'Python test,Python test 2;query=test;/path/')

IntegrationTests = test_wsgiref.IntegrationTests()
test_environ()
