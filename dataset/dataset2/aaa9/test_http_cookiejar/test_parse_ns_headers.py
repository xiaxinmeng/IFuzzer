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

def test_parse_ns_headers():
    HeaderTests.assertEqual(parse_ns_headers(['foo=bar; path=/; domain']), [[('foo', 'bar'), ('path', '/'), ('domain', None), ('version', '0')]])
    HeaderTests.assertEqual(parse_ns_headers(['foo=bar; expires=Foo Bar 12 33:22:11 2000']), [[('foo', 'bar'), ('expires', None), ('version', '0')]])
    HeaderTests.assertEqual(parse_ns_headers(['foo']), [[('foo', None), ('version', '0')]])
    HeaderTests.assertEqual(parse_ns_headers(['foo=bar; expires']), [[('foo', 'bar'), ('expires', None), ('version', '0')]])
    HeaderTests.assertEqual(parse_ns_headers(['foo=bar; version']), [[('foo', 'bar'), ('version', None)]])
    HeaderTests.assertEqual(parse_ns_headers(['']), [])

HeaderTests = test_http_cookiejar.HeaderTests()
test_parse_ns_headers()
