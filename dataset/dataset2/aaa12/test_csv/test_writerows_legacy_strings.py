import copy
import sys
import unittest
from io import StringIO
from tempfile import TemporaryFile
import csv
import gc
import pickle
from test import support
from test.support import warnings_helper
from itertools import permutations
from textwrap import dedent
from collections import OrderedDict
import _testcapi
import itertools
import array
import array
import array
import array, string
import test_csv

@support.cpython_only
@support.requires_legacy_unicode_capi
@warnings_helper.ignore_warnings(category=DeprecationWarning)
def test_writerows_legacy_strings():
    import _testcapi
    c = _testcapi.unicode_legacy_string('a')
    with TemporaryFile('w+', newline='') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerows([[c]])
        fileobj.seek(0)
        Test_Csv.assertEqual(fileobj.read(), 'a\r\n')

Test_Csv = test_csv.Test_Csv()
test_writerows_legacy_strings()
