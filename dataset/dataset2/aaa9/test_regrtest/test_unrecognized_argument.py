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

def test_unrecognized_argument():
    ParseArgsTestCase.checkError(['--xxx'], 'usage:')

ParseArgsTestCase = test_regrtest.ParseArgsTestCase()
test_unrecognized_argument()
