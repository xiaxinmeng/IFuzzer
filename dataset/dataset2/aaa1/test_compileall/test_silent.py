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

def test_silent():
    script_helper.make_script(CommandLineTestsBase.pkgdir, 'crunchyfrog', 'bad(syntax')
    (_, quiet, _) = CommandLineTestsBase.assertRunNotOK('-q', CommandLineTestsBase.pkgdir)
    (_, silent, _) = CommandLineTestsBase.assertRunNotOK('-qq', CommandLineTestsBase.pkgdir)
    CommandLineTestsBase.assertNotEqual(b'', quiet)
    CommandLineTestsBase.assertEqual(b'', silent)

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_silent()
