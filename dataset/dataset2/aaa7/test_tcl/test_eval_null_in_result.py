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

def test_eval_null_in_result():
    tcl = TclTest.interp
    TclTest.assertEqual(tcl.eval('set a "a\\0b"'), 'a\x00b')

TclTest = test_tcl.TclTest()
test_eval_null_in_result()
