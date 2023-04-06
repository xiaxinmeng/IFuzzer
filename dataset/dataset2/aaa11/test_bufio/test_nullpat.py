import unittest
from test import support
from test.support import os_helper
import io
import _pyio as pyio
import test_bufio

def test_nullpat():
    BufferSizeTest.drive_one(b'\x00' * 1000)

BufferSizeTest = test_bufio.BufferSizeTest()
test_nullpat()
