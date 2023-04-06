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

def test_testdir():
    ns = libregrtest._parse_args(['--testdir', 'foo'])
    ParseArgsTestCase.assertEqual(ns.testdir, os.path.join(os_helper.SAVEDCWD, 'foo'))
    ParseArgsTestCase.checkError(['--testdir'], 'expected one argument')

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_testdir()
