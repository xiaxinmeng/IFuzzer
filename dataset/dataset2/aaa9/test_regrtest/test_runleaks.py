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

def test_runleaks():
    for opt in ('-L', '--runleaks'):
        with ParseArgsTestCase.subTest(opt=opt):
            ns = libregrtest._parse_args([opt])
            ParseArgsTestCase.assertTrue(ns.runleaks)

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_runleaks()
