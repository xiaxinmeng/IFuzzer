import array
import unittest
from test.support import get_attribute
from test.support.import_helper import import_module
import os, struct
import pty
import test_ioctl

def test_ioctl_mutate():
    IoctlTests._check_ioctl_mutate_len()

IoctlTests = test_ioctl.IoctlTests()
test_ioctl_mutate()
