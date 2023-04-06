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

def test_process_smtputf8_message():
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'EHLO example')
    for mail_parameters in [b'', b'BODY=8BITMIME SMTPUTF8']:
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'MAIL from: <a@example> ' + mail_parameters)
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'250')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'rcpt to:<b@example.com>')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'250')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'data')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'354')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'c\r\n.')
        if mail_parameters == b'':
            SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last, b'250 OK\r\n')
        else:
            SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last, b'250 SMTPUTF8 message okish\r\n')

SMTPDChannelTestWithEnableSMTPUTF8True = test_smtpd.SMTPDChannelTestWithEnableSMTPUTF8True()
SMTPDChannelTestWithEnableSMTPUTF8True.setUp()
test_process_smtputf8_message()
