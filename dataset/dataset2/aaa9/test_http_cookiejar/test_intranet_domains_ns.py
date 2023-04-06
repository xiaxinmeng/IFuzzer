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

def test_intranet_domains_ns():
    c = CookieJar(DefaultCookiePolicy(rfc2965=False))
    test_http_cookiejar.interact_netscape(c, 'http://example/', 'foo1=bar')
    cookie = test_http_cookiejar.interact_netscape(c, 'http://example/', 'foo2=bar; domain=.local')
    LWPCookieTests.assertEqual(len(c), 2)
    LWPCookieTests.assertIn('foo1=bar', cookie)
    cookie = test_http_cookiejar.interact_netscape(c, 'http://example/')
    LWPCookieTests.assertIn('foo2=bar', cookie)
    LWPCookieTests.assertEqual(len(c), 2)

LWPCookieTests = test_http_cookiejar.LWPCookieTests()
test_intranet_domains_ns()
