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

def test_start():
    for opt in ('-S', '--start'):
        with ParseArgsTestCase.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, 'foo'])
            ParseArgsTestCase.assertEqual(ns.start, 'foo')
            ParseArgsTestCase.checkError([opt], 'expected one argument')

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_start()
