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

def test_validated_hello():
    (out, err) = test_wsgiref.run_amock(validator(test_wsgiref.hello_app))
    IntegrationTests.check_hello(out, has_length=False)

IntegrationTests = test_wsgiref.IntegrationTests()
test_validated_hello()
