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

def test_decode_data_and_enable_SMTPUTF8_raises():
    SMTPDServerTest.assertRaises(ValueError, smtpd.SMTPChannel, SMTPDServerTest.server, SMTPDServerTest.channel.conn, SMTPDServerTest.channel.addr, enable_SMTPUTF8=True, decode_data=True)

SMTPDServerTest = test_smtpd.SMTPDServerTest()
SMTPDServerTest.setUp()
test_decode_data_and_enable_SMTPUTF8_raises()
