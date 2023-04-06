import os
import select
import signal
import subprocess
import sys
import time
import unittest
import _io
import _pyio
import test_file_eintr

def test_readline():
    """readline() must handle signals and not lose data."""
    TestFileIOSignalInterrupt._test_reading(data_to_write=b'hello, world!', read_and_verify_code=TestFileIOSignalInterrupt._READING_CODE_TEMPLATE.format(read_method_name='readline', expected='hello, world!\n'))

TestFileIOSignalInterrupt = test_file_eintr.TestFileIOSignalInterrupt()
test_readline()
