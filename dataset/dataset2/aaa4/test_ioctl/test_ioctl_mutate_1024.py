import array
import unittest
from test.support import get_attribute
from test.support.import_helper import import_module
import os, struct
import pty
import test_ioctl

def test_ioctl_mutate_1024():
    IoctlTests._check_ioctl_mutate_len(1024)

IoctlTests = test_ioctl.IoctlTests()
test_ioctl_mutate_1024()
