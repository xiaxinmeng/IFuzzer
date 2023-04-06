import os
import re
import test.support
from test.support import os_helper
from test.support import warnings_helper
import time
import unittest
import urllib.request
import pathlib
from http.cookiejar import time2isoz, http2time, iso2time, time2netscape, parse_ns_headers, join_header_words, split_header_words, Cookie, CookieJar, DefaultCookiePolicy, LWPCookieJar, MozillaCookieJar, LoadError, lwp_cookie_str, DEFAULT_HTTP_PORT, escape_path, reach, is_HDN, domain_match, user_domain_match, request_path, request_port, request_host
import traceback, io
import email
import test_http_cookiejar

def test_request_port():
    req = urllib.request.Request('http://www.acme.com:1234/', headers={'Host': 'www.acme.com:4321'})
    CookieTests.assertEqual(request_port(req), '1234')
    req = urllib.request.Request('http://www.acme.com/', headers={'Host': 'www.acme.com:4321'})
    CookieTests.assertEqual(request_port(req), DEFAULT_HTTP_PORT)

CookieTests = test_http_cookiejar.CookieTests()
test_request_port()
