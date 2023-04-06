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

def test_run_code():
    expected_ns = test_runpy.example_namespace.copy()
    expected_ns.update({'__loader__': None})

    def create_ns(init_globals):
        return test_runpy._run_code(test_runpy.example_source, {}, init_globals)
    ExecutionLayerTestCase.check_code_execution(create_ns, expected_ns)

ExecutionLayerTestCase = test_runpy.ExecutionLayerTestCase()
test_run_code()
