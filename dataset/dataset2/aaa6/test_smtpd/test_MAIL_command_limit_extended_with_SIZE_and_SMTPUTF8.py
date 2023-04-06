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

def test_MAIL_command_limit_extended_with_SIZE_and_SMTPUTF8():
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'ehlo example')
    fill_len = 512 + 26 + 10 - len('mail from:<@example>')
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'MAIL from:<' + b'a' * (fill_len + 1) + b'@example>')
    SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last, b'500 Error: line too long\r\n')
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'MAIL from:<' + b'a' * fill_len + b'@example>')
    SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last, b'250 OK\r\n')

SMTPDChannelTestWithEnableSMTPUTF8True = test_smtpd.SMTPDChannelTestWithEnableSMTPUTF8True()
SMTPDChannelTestWithEnableSMTPUTF8True.setUp()
test_MAIL_command_limit_extended_with_SIZE_and_SMTPUTF8()
