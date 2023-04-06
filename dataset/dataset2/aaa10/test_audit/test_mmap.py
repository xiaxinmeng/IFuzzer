import subprocess
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_audit

def test_mmap():
    AuditTest.do_test('test_mmap')

AuditTest = test_audit.AuditTest()
test_mmap()
