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

def test_wsgi_input():

    def bad_app(e, s):
        e['wsgi.input'].read()
        s('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
        return [b'data']
    (out, err) = test_wsgiref.run_amock(validator(bad_app))
    IntegrationTests.assertTrue(out.endswith(b'A server error occurred.  Please contact the administrator.'))
    IntegrationTests.assertEqual(err.splitlines()[-2], 'AssertionError')

IntegrationTests = test_wsgiref.IntegrationTests()
test_wsgi_input()
