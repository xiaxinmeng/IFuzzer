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

def test_escape_path():
    cases = [('/foo%2f/bar', '/foo%2F/bar'), ('/foo%2F/bar', '/foo%2F/bar'), ('/foo%%/bar', '/foo%%/bar'), ('/fo%19o/bar', '/fo%19o/bar'), ('/fo%7do/bar', '/fo%7Do/bar'), ('/foo/bar&', '/foo/bar&'), ('/foo//bar', '/foo//bar'), ('~/foo/bar', '~/foo/bar'), ('/foo\x19/bar', '/foo%19/bar'), ('/}foo/bar', '/%7Dfoo/bar'), ('/foo/barü', '/foo/bar%C3%BC'), ('/foo/barꯍ', '/foo/bar%EA%AF%8D')]
    for (arg, result) in cases:
        CookieTests.assertEqual(escape_path(arg), result)

CookieTests = test_http_cookiejar.CookieTests()
test_escape_path()
