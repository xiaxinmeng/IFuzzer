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

def test_single():
    for opt in ('-s', '--single'):
        with ParseArgsTestCase.subTest(opt=opt):
            ns = libregrtest._parse_args([opt])
            ParseArgsTestCase.assertTrue(ns.single)
            ParseArgsTestCase.checkError([opt, '-f', 'foo'], "don't go together")

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_single()
