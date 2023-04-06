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

def test_broken_connect():
    SMTPDChannelTest.assertRaises(test_smtpd.DummyDispatcherBroken, test_smtpd.BrokenDummyServer, (socket_helper.HOST, 0), ('b', 0), decode_data=True)

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
test_broken_connect()
