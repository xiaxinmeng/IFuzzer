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

def test_readwriteexc():
    tr1 = test_asyncore.exitingdummy()
    HelperFunctionTests.assertRaises(asyncore.ExitNow, asyncore.read, tr1)
    HelperFunctionTests.assertRaises(asyncore.ExitNow, asyncore.write, tr1)
    HelperFunctionTests.assertRaises(asyncore.ExitNow, asyncore._exception, tr1)
    tr2 = test_asyncore.crashingdummy()
    asyncore.read(tr2)
    HelperFunctionTests.assertEqual(tr2.error_handled, True)
    tr2 = test_asyncore.crashingdummy()
    asyncore.write(tr2)
    HelperFunctionTests.assertEqual(tr2.error_handled, True)
    tr2 = test_asyncore.crashingdummy()
    asyncore._exception(tr2)
    HelperFunctionTests.assertEqual(tr2.error_handled, True)

HelperFunctionTests = test_asyncore.HelperFunctionTests()
test_readwriteexc()
