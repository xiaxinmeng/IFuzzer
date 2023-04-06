import unittest
import locale
import re
import subprocess
import sys
import os
import warnings
from test import support
from test.support import import_helper
from test.support import os_helper
import tkinter
from tkinter import Tcl
from _tkinter import TclError
from _testcapi import INT_MAX, PY_SSIZE_T_MAX
import test_tcl

def test_evalfile_null_in_result():
    tcl = TclTest.interp
    filename = os_helper.TESTFN_ASCII
    TclTest.addCleanup(os_helper.unlink, filename)
    with open(filename, 'w') as f:
        f.write('\n            set a "a\x00b"\n            set b "a\\0b"\n            ')
    tcl.evalfile(filename)
    TclTest.assertEqual(tcl.eval('set a'), 'a\x00b')
    TclTest.assertEqual(tcl.eval('set b'), 'a\x00b')

TclTest = test_tcl.TclTest()
test_evalfile_null_in_result()
