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

def test_iso2time_formats():
    tests = ['1994-02-03 00:00:00 -0000', '1994-02-03 00:00:00 +0000', '1994-02-03 00:00:00', '1994-02-03', '1994-02-03T00:00:00', '19940203', '1994-02-02 24:00:00', '19940203T000000Z', '  1994-02-03 ', '  1994-02-03T00:00:00  ']
    test_t = 760233600
    for s in tests:
        DateTimeTests.assertEqual(iso2time(s), test_t, s)
        DateTimeTests.assertEqual(iso2time(s.lower()), test_t, s.lower())
        DateTimeTests.assertEqual(iso2time(s.upper()), test_t, s.upper())

DateTimeTests = test_http_cookiejar.DateTimeTests()
test_iso2time_formats()
