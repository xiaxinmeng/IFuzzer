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

def test_eval_surrogates_in_result():
    tcl = TclTest.interp
    TclTest.assertIn(tcl.eval('set a "<\\ud83d\\udcbb>"'), '<💻>')

TclTest = test_tcl.TclTest()
test_eval_surrogates_in_result()
