import compileall
import contextlib
import filecmp
import importlib.util
import io
import itertools
import os
import pathlib
import py_compile
import shutil
import struct
import sys
import tempfile
import test.test_importlib.util
import time
import unittest
from unittest import mock, skipUnless
from concurrent.futures import ProcessPoolExecutor
from test import support
from test.support import os_helper
from test.support import script_helper

import test_compileall

def test_compiles_as_much_as_possible():
    bingfn = script_helper.make_script(CommandLineTestsBase.pkgdir, 'bing', 'syntax(error')
    (rc, out, err) = CommandLineTestsBase.assertRunNotOK('nosuchfile', CommandLineTestsBase.initfn, bingfn, CommandLineTestsBase.barfn)
    CommandLineTestsBase.assertRegex(out, b'rror')
    CommandLineTestsBase.assertNotCompiled(bingfn)
    CommandLineTestsBase.assertCompiled(CommandLineTestsBase.initfn)
    CommandLineTestsBase.assertCompiled(CommandLineTestsBase.barfn)

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
CommandLineTestsBase.setUp()
test_compiles_as_much_as_possible()
