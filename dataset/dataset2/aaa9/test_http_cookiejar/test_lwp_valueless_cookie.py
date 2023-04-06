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

def test_lwp_valueless_cookie():
    filename = os_helper.TESTFN
    c = LWPCookieJar()
    test_http_cookiejar.interact_netscape(c, 'http://www.acme.com/', 'boo')
    FileCookieJarTests.assertEqual(c._cookies['www.acme.com']['/']['boo'].value, None)
    try:
        c.save(filename, ignore_discard=True)
        c = LWPCookieJar()
        c.load(filename, ignore_discard=True)
    finally:
        try:
            os.unlink(filename)
        except OSError:
            pass
    FileCookieJarTests.assertEqual(c._cookies['www.acme.com']['/']['boo'].value, None)

FileCookieJarTests = test_http_cookiejar.FileCookieJarTests()
test_lwp_valueless_cookie()
