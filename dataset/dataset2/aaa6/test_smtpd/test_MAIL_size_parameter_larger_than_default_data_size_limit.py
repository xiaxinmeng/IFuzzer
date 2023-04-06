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

def test_MAIL_size_parameter_larger_than_default_data_size_limit():
    SMTPDChannelTest.channel.data_size_limit = 1048
    SMTPDChannelTest.write_line(b'EHLO example')
    SMTPDChannelTest.write_line(b'MAIL FROM:<eggs@example> SIZE=2096')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'552 Error: message size exceeds fixed maximum message size\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_MAIL_size_parameter_larger_than_default_data_size_limit()
