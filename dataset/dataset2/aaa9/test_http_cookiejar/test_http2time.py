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

def test_http2time():

    def parse_date(text):
        return time.gmtime(http2time(text))[:6]
    DateTimeTests.assertEqual(parse_date('01 Jan 2001'), (2001, 1, 1, 0, 0, 0.0))
    DateTimeTests.assertEqual(parse_date('03-Feb-20'), (2020, 2, 3, 0, 0, 0.0))
    DateTimeTests.assertEqual(parse_date('03-Feb-98'), (1998, 2, 3, 0, 0, 0.0))

DateTimeTests = test_http_cookiejar.DateTimeTests()
test_http2time()
