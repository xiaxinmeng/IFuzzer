import unittest
from test import support
from test.support import import_helper
from test.support import socket_helper
import smtplib
import socket
import test_smtpnet

def test_connect_default_port():
    support.get_attribute(smtplib, 'SMTP_SSL')
    with socket_helper.transient_internet(SmtpSSLTest.testServer):
        server = smtplib.SMTP_SSL(SmtpSSLTest.testServer)
        server.ehlo()
        server.quit()

SmtpSSLTest = test_smtpnet.SmtpSSLTest()
test_connect_default_port()
