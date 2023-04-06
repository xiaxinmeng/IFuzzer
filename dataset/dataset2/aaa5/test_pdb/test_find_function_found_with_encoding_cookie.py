import doctest
import os
import pdb
import sys
import types
import codecs
import unittest
import subprocess
import textwrap
from contextlib import ExitStack
from io import StringIO
from test.support import os_helper
from test.test_doctest import _FakeInput
from unittest.mock import patch
from test import test_pdb
import test_pdb

def test_find_function_found_with_encoding_cookie():
    PdbTestCase._assert_find_function('# coding: iso-8859-15\ndef foo():\n    pass\n\ndef bœr():\n    pass\n\ndef quux():\n    pass\n'.encode('iso-8859-15'), 'bœr', ('bœr', 5))

PdbTestCase = test_pdb.PdbTestCase()
test_find_function_found_with_encoding_cookie()
