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

def test_unknown_command():
    SMTPDChannelTest.write_line(b'UNKNOWN_CMD')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'500 Error: command "UNKNOWN_CMD" not ' + b'recognized\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_unknown_command()
