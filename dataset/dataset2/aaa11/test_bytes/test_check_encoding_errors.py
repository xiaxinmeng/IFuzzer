import array
import os
import re
import sys
import copy
import functools
import pickle
import tempfile
import textwrap
import unittest
import test.support
from test.support import import_helper
from test.support import warnings_helper
import test.string_tests
import test.list_tests
from test.support import bigaddrspacetest, MAX_Py_ssize_t
from test.support.script_helper import assert_python_failure
from ctypes import pythonapi, py_object
from ctypes import c_int, c_uint, c_long, c_ulong, c_size_t, c_ssize_t, c_char_p
from _testcapi import getbuffer_with_null_view
import test_bytes

def test_check_encoding_errors():
    invalid = 'Boom, Shaka Laka, Boom!'
    encodings = ('ascii', 'utf8', 'latin1')
    code = textwrap.dedent(f"\n            import sys\n            type2test = {BaseBytesTest.type2test.__name__}\n            encodings = {encodings!r}\n\n            for data in ('', 'short string'):\n                try:\n                    type2test(data, encoding={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(21)\n\n                for encoding in encodings:\n                    try:\n                        type2test(data, encoding=encoding, errors={invalid!r})\n                    except LookupError:\n                        pass\n                    else:\n                        sys.exit(22)\n\n            for data in (b'', b'short string'):\n                data = type2test(data)\n                print(repr(data))\n                try:\n                    data.decode(encoding={invalid!r})\n                except LookupError:\n                    sys.exit(10)\n                else:\n                    sys.exit(23)\n\n                try:\n                    data.decode(errors={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(24)\n\n                for encoding in encodings:\n                    try:\n                        data.decode(encoding=encoding, errors={invalid!r})\n                    except LookupError:\n                        pass\n                    else:\n                        sys.exit(25)\n\n            sys.exit(10)\n        ")
    proc = assert_python_failure('-X', 'dev', '-c', code)
    BaseBytesTest.assertEqual(proc.rc, 10, proc)

BaseBytesTest = test_bytes.BaseBytesTest()
test_check_encoding_errors()
