import subprocess
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_audit

def test_block_add_hook():
    AuditTest.do_test('test_block_add_hook')

AuditTest = test_audit.AuditTest()
test_block_add_hook()
