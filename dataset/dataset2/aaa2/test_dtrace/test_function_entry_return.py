import dis
import os.path
import re
import subprocess
import sys
import types
import unittest
from test.support import findfile, run_unittest
import test_dtrace

def test_function_entry_return():
    TraceTests.run_case('call_stack')

TraceTests = test_dtrace.TraceTests()
TraceTests.setUp()
test_function_entry_return()
