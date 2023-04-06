from collections import OrderedDict
import os
import pickle
import random
import re
import subprocess
import sys
import textwrap
import threading
import time
import unittest
import weakref
import importlib.machinery
import importlib.util
from test import support
from test.support import MISSING_C_DOCSTRINGS
from test.support import import_helper
from test.support import threading_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_failure, assert_python_ok
import _posixsubprocess
import _testinternalcapi
from _testcapi import MyList
from _testcapi import MyList
from _testcapi import pynumber_tobase
import builtins
import binascii
import test_capi

@unittest.skipIf(MISSING_C_DOCSTRINGS, 'Signature information for builtins requires docstrings')
def test_docstring_signature_parsing():
    CAPITest.assertEqual(test_capi._testcapi.no_docstring.__doc__, None)
    CAPITest.assertEqual(test_capi._testcapi.no_docstring.__text_signature__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_empty.__doc__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_empty.__text_signature__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_no_signature.__doc__, 'This docstring has no signature.')
    CAPITest.assertEqual(test_capi._testcapi.docstring_no_signature.__text_signature__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_invalid_signature.__doc__, 'docstring_with_invalid_signature($module, /, boo)\n\nThis docstring has an invalid signature.')
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_invalid_signature.__text_signature__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_invalid_signature2.__doc__, 'docstring_with_invalid_signature2($module, /, boo)\n\n--\n\nThis docstring also has an invalid signature.')
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_invalid_signature2.__text_signature__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_signature.__doc__, 'This docstring has a valid signature.')
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_signature.__text_signature__, '($module, /, sig)')
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_signature_but_no_doc.__doc__, None)
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_signature_but_no_doc.__text_signature__, '($module, /, sig)')
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_signature_and_extra_newlines.__doc__, '\nThis docstring has a valid signature and some extra newlines.')
    CAPITest.assertEqual(test_capi._testcapi.docstring_with_signature_and_extra_newlines.__text_signature__, '($module, /, parameter)')

CAPITest = test_capi.CAPITest()
test_docstring_signature_parsing()
