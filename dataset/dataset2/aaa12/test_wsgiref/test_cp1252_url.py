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

def test_cp1252_url():

    def app(e, s):
        s('200 OK', [('Content-Type', 'text/plain'), ('Date', 'Wed, 24 Dec 2008 13:29:32 GMT')])
        return [e['PATH_INFO'].encode('latin1')]
    (out, err) = test_wsgiref.run_amock(validator(app), data=b'GET /\x80%80 HTTP/1.0')
    IntegrationTests.assertEqual([b'HTTP/1.0 200 OK', mock.ANY, b'Content-Type: text/plain', b'Date: Wed, 24 Dec 2008 13:29:32 GMT', b'', b'/\x80\x80'], out.splitlines())

IntegrationTests = test_wsgiref.IntegrationTests()
test_cp1252_url()
