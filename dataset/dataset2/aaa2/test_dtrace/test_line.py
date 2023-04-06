import dis
import os.path
import re
import subprocess
import sys
import types
import unittest
from test.support import findfile, run_unittest
import test_dtrace

def test_line():
    TraceTests.run_case('line')

TraceTests = test_dtrace.TraceTests()
test_line()
