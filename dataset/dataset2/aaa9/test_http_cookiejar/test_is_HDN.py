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

def test_is_HDN():
    CookieTests.assertTrue(is_HDN('foo.bar.com'))
    CookieTests.assertTrue(is_HDN('1foo2.3bar4.5com'))
    CookieTests.assertFalse(is_HDN('192.168.1.1'))
    CookieTests.assertFalse(is_HDN(''))
    CookieTests.assertFalse(is_HDN('.'))
    CookieTests.assertFalse(is_HDN('.foo.bar.com'))
    CookieTests.assertFalse(is_HDN('..foo'))
    CookieTests.assertFalse(is_HDN('foo.'))

CookieTests = test_http_cookiejar.CookieTests()
test_is_HDN()
