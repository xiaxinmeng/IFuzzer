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

def test_http2time_garbage():
    for test in ['', 'Garbage', 'Mandag 16. September 1996', '01-00-1980', '01-13-1980', '00-01-1980', '32-01-1980', '01-01-1980 25:00:00', '01-01-1980 00:61:00', '01-01-1980 00:00:62', '08-Oct-3697739', '08-01-3697739', '09 Feb 19942632 22:23:32 GMT', 'Wed, 09 Feb 1994834 22:23:32 GMT']:
        DateTimeTests.assertIsNone(http2time(test), 'http2time(%s) is not None\nhttp2time(test) %s' % (test, http2time(test)))

DateTimeTests = test_http_cookiejar.DateTimeTests()
test_http2time_garbage()
