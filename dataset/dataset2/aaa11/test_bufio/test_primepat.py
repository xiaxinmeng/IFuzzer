import unittest
from test import support
from test.support import os_helper
import io
import _pyio as pyio
import test_bufio

def test_primepat():
    BufferSizeTest.drive_one(b'1234567890\x00\x01\x02\x03\x04\x05\x06')

BufferSizeTest = test_bufio.BufferSizeTest()
test_primepat()
