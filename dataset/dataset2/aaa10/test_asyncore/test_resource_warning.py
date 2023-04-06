import asyncore
import unittest
import select
import os
import socket
import sys
import time
import errno
import struct
import threading
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
from test.support import warnings_helper
from io import BytesIO
import test_asyncore

def test_resource_warning():
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    f = asyncore.file_wrapper(fd)
    os.close(fd)
    with warnings_helper.check_warnings(('', ResourceWarning)):
        f = None
        support.gc_collect()

FileWrapperTest = test_asyncore.FileWrapperTest()
test_resource_warning()
