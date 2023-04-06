from unittest import TestCase
from unittest.case import _AssertRaisesContext
import sys
import traceback

manager = _AssertRaisesContext(Exception, TestCase(), 'aaa')