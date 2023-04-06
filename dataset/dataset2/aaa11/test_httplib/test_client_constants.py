import errno
from http import client, HTTPStatus
import io
import itertools
import os
import array
import re
import socket
import threading
import warnings
import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import warnings_helper
from test.ssl_servers import make_https_server
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import test_httplib

def test_client_constants():
    expected = ['CONTINUE', 'SWITCHING_PROTOCOLS', 'PROCESSING', 'OK', 'CREATED', 'ACCEPTED', 'NON_AUTHORITATIVE_INFORMATION', 'NO_CONTENT', 'RESET_CONTENT', 'PARTIAL_CONTENT', 'MULTI_STATUS', 'IM_USED', 'MULTIPLE_CHOICES', 'MOVED_PERMANENTLY', 'FOUND', 'SEE_OTHER', 'NOT_MODIFIED', 'USE_PROXY', 'TEMPORARY_REDIRECT', 'BAD_REQUEST', 'UNAUTHORIZED', 'PAYMENT_REQUIRED', 'FORBIDDEN', 'NOT_FOUND', 'METHOD_NOT_ALLOWED', 'NOT_ACCEPTABLE', 'PROXY_AUTHENTICATION_REQUIRED', 'REQUEST_TIMEOUT', 'CONFLICT', 'GONE', 'LENGTH_REQUIRED', 'PRECONDITION_FAILED', 'REQUEST_ENTITY_TOO_LARGE', 'REQUEST_URI_TOO_LONG', 'UNSUPPORTED_MEDIA_TYPE', 'REQUESTED_RANGE_NOT_SATISFIABLE', 'EXPECTATION_FAILED', 'IM_A_TEAPOT', 'MISDIRECTED_REQUEST', 'UNPROCESSABLE_ENTITY', 'LOCKED', 'FAILED_DEPENDENCY', 'UPGRADE_REQUIRED', 'PRECONDITION_REQUIRED', 'TOO_MANY_REQUESTS', 'REQUEST_HEADER_FIELDS_TOO_LARGE', 'UNAVAILABLE_FOR_LEGAL_REASONS', 'INTERNAL_SERVER_ERROR', 'NOT_IMPLEMENTED', 'BAD_GATEWAY', 'SERVICE_UNAVAILABLE', 'GATEWAY_TIMEOUT', 'HTTP_VERSION_NOT_SUPPORTED', 'INSUFFICIENT_STORAGE', 'NOT_EXTENDED', 'NETWORK_AUTHENTICATION_REQUIRED', 'EARLY_HINTS', 'TOO_EARLY']
    for const in expected:
        with OfflineTest.subTest(constant=const):
            OfflineTest.assertTrue(hasattr(client, const))

OfflineTest = test_httplib.OfflineTest()
test_client_constants()
