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

def test_wrong_domain():
    c = CookieJar()
    test_http_cookiejar.interact_2965(c, 'http://www.nasty.com/', 'foo=bar; domain=friendly.org; Version="1"')
    CookieTests.assertEqual(len(c), 0)

CookieTests = test_http_cookiejar.CookieTests()
test_wrong_domain()
