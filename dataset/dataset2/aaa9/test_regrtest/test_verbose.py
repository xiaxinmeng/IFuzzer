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

def test_verbose():
    ns = libregrtest._parse_args(['-v'])
    ParseArgsTestCase.assertEqual(ns.verbose, 1)
    ns = libregrtest._parse_args(['-vvv'])
    ParseArgsTestCase.assertEqual(ns.verbose, 3)
    ns = libregrtest._parse_args(['--verbose'])
    ParseArgsTestCase.assertEqual(ns.verbose, 1)
    ns = libregrtest._parse_args(['--verbose'] * 3)
    ParseArgsTestCase.assertEqual(ns.verbose, 3)
    ns = libregrtest._parse_args([])
    ParseArgsTestCase.assertEqual(ns.verbose, 0)

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_verbose()
