from io import BytesIO
import os
import platform
import sys
import sysconfig
import unittest
import traceback
from xml.parsers import expat
from xml.parsers.expat import errors
from test.support import sortdict
import test_pyexpat

def test_1000_bytes():
    ChardataBufferTest.assertEqual(ChardataBufferTest.small_buffer_test(1000), 1)

ChardataBufferTest = test_pyexpat.ChardataBufferTest()
test_1000_bytes()
