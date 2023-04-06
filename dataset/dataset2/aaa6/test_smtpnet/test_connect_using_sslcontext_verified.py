import unittest
from test import support
from test.support import import_helper
from test.support import socket_helper
import smtplib
import socket
import test_smtpnet

def test_connect_using_sslcontext_verified():
    with socket_helper.transient_internet(SmtpSSLTest.testServer):
        can_verify = test_smtpnet.check_ssl_verifiy(SmtpSSLTest.testServer, SmtpSSLTest.remotePort)
        if not can_verify:
            SmtpSSLTest.skipTest("SSL certificate can't be verified")
    support.get_attribute(smtplib, 'SMTP_SSL')
    context = test_smtpnet.ssl.create_default_context()
    with socket_helper.transient_internet(SmtpSSLTest.testServer):
        server = smtplib.SMTP_SSL(SmtpSSLTest.testServer, SmtpSSLTest.remotePort, context=context)
        server.ehlo()
        server.quit()

SmtpSSLTest = test_smtpnet.SmtpSSLTest()
test_connect_using_sslcontext_verified()
