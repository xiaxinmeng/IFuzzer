from test import support
from test.support import socket_helper
from contextlib import contextmanager
import imaplib
import os.path
import socketserver
import time
import calendar
import threading
import socket
from test.support import verbose, run_with_tz, run_with_locale, cpython_only
from test.support import hashlib_helper
from test.support import threading_helper
from test.support import warnings_helper
import unittest
from unittest import mock
from datetime import datetime, timezone, timedelta
import ssl
import test_imaplib

@threading_helper.reap_threads
@cpython_only
def test_dump_ur():
    untagged_resp_dict = {'READ-WRITE': [b'']}
    with ThreadedNetworkedTests.reaped_server(test_imaplib.SimpleIMAPHandler) as server:
        with ThreadedNetworkedTests.imap_class(*server.server_address) as imap:
            with mock.patch.object(imap, '_mesg') as mock_mesg:
                imap._dump_ur(untagged_resp_dict)
                mock_mesg.assert_called_with("untagged responses dump:READ-WRITE: [b'']")

ThreadedNetworkedTests = test_imaplib.ThreadedNetworkedTests()
test_dump_ur()
