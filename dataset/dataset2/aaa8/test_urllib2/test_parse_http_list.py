import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import warnings_helper
from test import test_urllib
import os
import io
import socket
import array
import sys
import tempfile
import subprocess
import urllib.request
from urllib.request import Request, OpenerDirector, HTTPBasicAuthHandler, HTTPPasswordMgrWithPriorAuth, _parse_proxy, _proxy_bypass_macosx_sysconf, AbstractDigestAuthHandler
from urllib.parse import urlparse
import urllib.error
import http.client
import email, copy
from urllib.error import URLError
import ftplib
import email.utils
from http.cookiejar import CookieJar
from test.test_http_cookiejar import interact_netscape
import base64
import test_urllib2

def test_parse_http_list():
    tests = [('a,b,c', ['a', 'b', 'c']), ('path"o,l"og"i"cal, example', ['path"o,l"og"i"cal', 'example']), ('a, b, "c", "d", "e,f", g, h', ['a', 'b', '"c"', '"d"', '"e,f"', 'g', 'h']), ('a="b\\"c", d="e\\,f", g="h\\\\i"', ['a="b"c"', 'd="e,f"', 'g="h\\i"'])]
    for (string, list) in tests:
        TrivialTests.assertEqual(urllib.request.parse_http_list(string), list)

TrivialTests = test_urllib2.TrivialTests()
test_parse_http_list()
