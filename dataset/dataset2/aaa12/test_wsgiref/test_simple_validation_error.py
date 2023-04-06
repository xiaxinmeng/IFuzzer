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

def test_simple_validation_error():

    def bad_app(environ, start_response):
        start_response('200 OK', ('Content-Type', 'text/plain'))
        return ['Hello, world!']
    (out, err) = test_wsgiref.run_amock(validator(bad_app))
    IntegrationTests.assertTrue(out.endswith(b'A server error occurred.  Please contact the administrator.'))
    IntegrationTests.assertEqual(err.splitlines()[-2], "AssertionError: Headers (('Content-Type', 'text/plain')) must be of type list: <class 'tuple'>")

IntegrationTests = test_wsgiref.IntegrationTests()
test_simple_validation_error()
