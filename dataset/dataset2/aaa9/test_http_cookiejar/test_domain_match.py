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

def test_domain_match():
    CookieTests.assertTrue(domain_match('192.168.1.1', '192.168.1.1'))
    CookieTests.assertFalse(domain_match('192.168.1.1', '.168.1.1'))
    CookieTests.assertTrue(domain_match('x.y.com', 'x.Y.com'))
    CookieTests.assertTrue(domain_match('x.y.com', '.Y.com'))
    CookieTests.assertFalse(domain_match('x.y.com', 'Y.com'))
    CookieTests.assertTrue(domain_match('a.b.c.com', '.c.com'))
    CookieTests.assertFalse(domain_match('.c.com', 'a.b.c.com'))
    CookieTests.assertTrue(domain_match('example.local', '.local'))
    CookieTests.assertFalse(domain_match('blah.blah', ''))
    CookieTests.assertFalse(domain_match('', '.rhubarb.rhubarb'))
    CookieTests.assertTrue(domain_match('', ''))
    CookieTests.assertTrue(user_domain_match('acme.com', 'acme.com'))
    CookieTests.assertFalse(user_domain_match('acme.com', '.acme.com'))
    CookieTests.assertTrue(user_domain_match('rhubarb.acme.com', '.acme.com'))
    CookieTests.assertTrue(user_domain_match('www.rhubarb.acme.com', '.acme.com'))
    CookieTests.assertTrue(user_domain_match('x.y.com', 'x.Y.com'))
    CookieTests.assertTrue(user_domain_match('x.y.com', '.Y.com'))
    CookieTests.assertFalse(user_domain_match('x.y.com', 'Y.com'))
    CookieTests.assertTrue(user_domain_match('y.com', 'Y.com'))
    CookieTests.assertFalse(user_domain_match('.y.com', 'Y.com'))
    CookieTests.assertTrue(user_domain_match('.y.com', '.Y.com'))
    CookieTests.assertTrue(user_domain_match('x.y.com', '.com'))
    CookieTests.assertFalse(user_domain_match('x.y.com', 'com'))
    CookieTests.assertFalse(user_domain_match('x.y.com', 'm'))
    CookieTests.assertFalse(user_domain_match('x.y.com', '.m'))
    CookieTests.assertFalse(user_domain_match('x.y.com', ''))
    CookieTests.assertFalse(user_domain_match('x.y.com', '.'))
    CookieTests.assertTrue(user_domain_match('192.168.1.1', '192.168.1.1'))
    CookieTests.assertFalse(user_domain_match('192.168.1.1', '.168.1.1'))
    CookieTests.assertFalse(user_domain_match('192.168.1.1', '.'))
    CookieTests.assertFalse(user_domain_match('192.168.1.1', ''))

CookieTests = test_http_cookiejar.CookieTests()
test_domain_match()
