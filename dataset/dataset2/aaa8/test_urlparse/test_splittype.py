import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splittype():
    splittype = urllib.parse._splittype
    Utility_Tests.assertEqual(splittype('type:opaquestring'), ('type', 'opaquestring'))
    Utility_Tests.assertEqual(splittype('opaquestring'), (None, 'opaquestring'))
    Utility_Tests.assertEqual(splittype(':opaquestring'), (None, ':opaquestring'))
    Utility_Tests.assertEqual(splittype('type:'), ('type', ''))
    Utility_Tests.assertEqual(splittype('type:opaque:string'), ('type', 'opaque:string'))


parse_qsl_test_cases = [
    ("", []),
    ("&", []),
    ("&&", []),
    ("=", [('', '')]),
    ("=a", [('', 'a')]),
    ("a", [('a', '')]),
    ("a=", [('a', '')]),
    ("&a=b", [('a', 'b')]),
    ("a=a+b&b=b+c", [('a', 'a b'), ('b', 'b c')]),
    ("a=1&a=2", [('a', '1'), ('a', '2')]),
    (b"", []),
    (b"&", []),
    (b"&&", []),
    (b"=", [(b'', b'')]),
    (b"=a", [(b'', b'a')]),
    (b"a", [(b'a', b'')]),
    (b"a=", [(b'a', b'')]),
    (b"&a=b", [(b'a', b'b')]),
    (b"a=a+b&b=b+c", [(b'a', b'a b'), (b'b', b'b c')]),
    (b"a=1&a=2", [(b'a', b'1'), (b'a', b'2')]),
    (";", []),
    (";;", []),
    (";a=b", [('a', 'b')]),
    ("a=a+b;b=b+c", [('a', 'a b'), ('b', 'b c')]),
    ("a=1;a=2", [('a', '1'), ('a', '2')]),
    (b";", []),
    (b";;", []),
    (b";a=b", [(b'a', b'b')]),
    (b"a=a+b;b=b+c", [(b'a', b'a b'), (b'b', b'b c')]),
    (b"a=1;a=2", [(b'a', b'1'), (b'a', b'2')]),
]
Utility_Tests = test_urlparse.Utility_Tests()
test_splittype()
