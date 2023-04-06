import unittest
import textwrap
from test import support, mock_socket
from test.support import socket_helper
from test.support import warnings_helper
import socket
import io
import smtpd
import asyncore
import test_smtpd

def test__all__():
    not_exported = {'program', 'Devnull', 'DEBUGSTREAM', 'NEWLINE', 'COMMASPACE', 'DATA_SIZE_DEFAULT', 'usage', 'Options', 'parseargs'}
    support.check__all__(MiscTestCase, smtpd, not_exported=not_exported)

MiscTestCase = test_smtpd.MiscTestCase()
test__all__()
