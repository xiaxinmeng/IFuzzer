import contextlib
import importlib.machinery, importlib.util
import os.path
import pathlib
import py_compile
import re
import signal
import subprocess
import sys
import tempfile
import textwrap
import unittest
import warnings
from test.support import no_tracing, verbose
from test.support.import_helper import forget, make_legacy_pyc, unload
from test.support.os_helper import create_empty_file, temp_dir
from test.support.script_helper import make_script, make_zip_script
import runpy
from runpy import _run_code, _run_module_code, run_module, run_path
import pkgutil
import test_runpy

def test_encoding():
    with temp_dir() as script_dir:
        filename = os.path.join(script_dir, 'script.py')
        with open(filename, 'w', encoding='latin1') as f:
            f.write('\n#coding:latin1\ns = "non-ASCII: hé"\n')
        result = run_path(filename)
        RunPathTestCase.assertEqual(result['s'], 'non-ASCII: hé')

RunPathTestCase = test_runpy.RunPathTestCase()
test_encoding()
