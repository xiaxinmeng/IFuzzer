import contextlib
import glob
import io
import os.path
import platform
import re
import subprocess
import sys
import sysconfig
import tempfile
import textwrap
import unittest
from test import libregrtest
from test import support
from test.support import os_helper
from test.libregrtest import utils
import test_regrtest

def test_two_options():
    ns = libregrtest._parse_args(['--quiet', '--exclude'])
    ParseArgsTestCase.assertTrue(ns.quiet)
    ParseArgsTestCase.assertEqual(ns.verbose, 0)
    ParseArgsTestCase.assertTrue(ns.exclude)

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_two_options()
