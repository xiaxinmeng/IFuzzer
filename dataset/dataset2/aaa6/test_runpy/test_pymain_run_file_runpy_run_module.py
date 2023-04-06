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

def test_pymain_run_file_runpy_run_module():
    tmp = TestExit.ham.parent
    run_module = tmp / 'run_module.py'
    run_module.write_text(textwrap.dedent('                import runpy\n                runpy.run_module("ham")\n                '))
    TestExit.assertSigInt([sys.executable, run_module], cwd=tmp)

TestExit = test_runpy.TestExit()
test_pymain_run_file_runpy_run_module()
