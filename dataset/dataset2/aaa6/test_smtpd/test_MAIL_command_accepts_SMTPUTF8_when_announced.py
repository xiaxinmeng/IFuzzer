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

def test_MAIL_command_accepts_SMTPUTF8_when_announced():
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'EHLO example')
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line('MAIL from: <naïve@example.com> BODY=8BITMIME SMTPUTF8'.encode('utf-8'))
    SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last, b'250 OK\r\n')

SMTPDChannelTestWithEnableSMTPUTF8True = test_smtpd.SMTPDChannelTestWithEnableSMTPUTF8True()
SMTPDChannelTestWithEnableSMTPUTF8True.setUp()
test_MAIL_command_accepts_SMTPUTF8_when_announced()
