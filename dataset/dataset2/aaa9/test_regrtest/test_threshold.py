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

def test_threshold():
    for opt in ('-t', '--threshold'):
        with ParseArgsTestCase.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, '1000'])
            ParseArgsTestCase.assertEqual(ns.threshold, 1000)
            ParseArgsTestCase.checkError([opt], 'expected one argument')
            ParseArgsTestCase.checkError([opt, 'foo'], 'invalid int value')

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_threshold()
