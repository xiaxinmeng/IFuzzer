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

def test_iso2time_garbage():
    for test in ['', 'Garbage', 'Thursday, 03-Feb-94 00:00:00 GMT', '1980-00-01', '1980-13-01', '1980-01-00', '1980-01-32', '1980-01-01 25:00:00', '1980-01-01 00:61:00', '01-01-1980 00:00:62', '01-01-1980T00:00:62', '19800101T250000Z']:
        DateTimeTests.assertIsNone(iso2time(test), 'iso2time(%r)' % test)

DateTimeTests = test_http_cookiejar.DateTimeTests()
test_iso2time_garbage()
