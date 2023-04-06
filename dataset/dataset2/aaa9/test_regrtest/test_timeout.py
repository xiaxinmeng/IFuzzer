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

def test_timeout():
    ns = libregrtest._parse_args(['--timeout', '4.2'])
    ParseArgsTestCase.assertEqual(ns.timeout, 4.2)
    ParseArgsTestCase.checkError(['--timeout'], 'expected one argument')
    ParseArgsTestCase.checkError(['--timeout', 'foo'], 'invalid float value')

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_timeout()
