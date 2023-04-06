import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

def test_pagesize():
    pagesize = test_resource.resource.getpagesize()
    ResourceTest.assertIsInstance(pagesize, int)
    ResourceTest.assertGreaterEqual(pagesize, 0)

ResourceTest = test_resource.ResourceTest()
test_pagesize()
