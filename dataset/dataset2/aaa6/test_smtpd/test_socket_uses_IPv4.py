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

def test_socket_uses_IPv4():
    server = smtpd.SMTPServer((socket_helper.HOSTv4, 0), (socket_helper.HOSTv6, 0))
    TestFamilyDetection.assertEqual(server.socket.family, socket.AF_INET)

TestFamilyDetection = test_smtpd.TestFamilyDetection()
test_socket_uses_IPv4()
