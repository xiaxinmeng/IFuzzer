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

def test_readlines():
    """readlines() must handle signals and not lose data."""
    TestFileIOSignalInterrupt._test_reading(data_to_write=b'hello\r\nworld!', read_and_verify_code=TestFileIOSignalInterrupt._READING_CODE_TEMPLATE.format(read_method_name='readlines', expected=['hello\n', 'world!\n']))

TestFileIOSignalInterrupt = test_file_eintr.TestFileIOSignalInterrupt()
test_readlines()
