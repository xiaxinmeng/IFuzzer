import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

def test_args():
    ResourceTest.assertRaises(TypeError, test_resource.resource.getrlimit)
    ResourceTest.assertRaises(TypeError, test_resource.resource.getrlimit, 42, 42)
    ResourceTest.assertRaises(TypeError, test_resource.resource.setrlimit)
    ResourceTest.assertRaises(TypeError, test_resource.resource.setrlimit, 42, 42, 42)

ResourceTest = test_resource.ResourceTest()
test_args()
