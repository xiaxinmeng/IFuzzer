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

def test_ietf_example_2():
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    test_http_cookiejar.interact_2965(c, 'http://www.acme.com/acme/ammo/specific', 'Part_Number="Rocket_Launcher_0001"; Version="1"; Path="/acme"', 'Part_Number="Riding_Rocket_0023"; Version="1"; Path="/acme/ammo"')
    cookie = test_http_cookiejar.interact_2965(c, 'http://www.acme.com/acme/ammo/...')
    LWPCookieTests.assertRegex(cookie, 'Riding_Rocket_0023.*Rocket_Launcher_0001')
    cookie = test_http_cookiejar.interact_2965(c, 'http://www.acme.com/acme/parts/')
    LWPCookieTests.assertIn('Rocket_Launcher_0001', cookie)
    LWPCookieTests.assertNotIn('Riding_Rocket_0023', cookie)

LWPCookieTests = test_http_cookiejar.LWPCookieTests()
test_ietf_example_2()
