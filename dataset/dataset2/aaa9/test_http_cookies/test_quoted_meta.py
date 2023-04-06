import copy
from test.support import run_unittest, run_doctest
import unittest
from http import cookies
import pickle
import test_http_cookies

def test_quoted_meta():
    C = cookies.SimpleCookie()
    C.load('Customer="WILE_E_COYOTE"; Version="1"; Path="/acme"')
    CookieTests.assertEqual(C['Customer'].value, 'WILE_E_COYOTE')
    CookieTests.assertEqual(C['Customer']['version'], '1')
    CookieTests.assertEqual(C['Customer']['path'], '/acme')
    CookieTests.assertEqual(C.output(['path']), 'Set-Cookie: Customer="WILE_E_COYOTE"; Path=/acme')
    CookieTests.assertEqual(C.js_output(), '\n        <script type="text/javascript">\n        <!-- begin hiding\n        document.cookie = "Customer=\\"WILE_E_COYOTE\\"; Path=/acme; Version=1";\n        // end hiding -->\n        </script>\n        ')
    CookieTests.assertEqual(C.js_output(['path']), '\n        <script type="text/javascript">\n        <!-- begin hiding\n        document.cookie = "Customer=\\"WILE_E_COYOTE\\"; Path=/acme";\n        // end hiding -->\n        </script>\n        ')

CookieTests = test_http_cookies.CookieTests()
test_quoted_meta()
