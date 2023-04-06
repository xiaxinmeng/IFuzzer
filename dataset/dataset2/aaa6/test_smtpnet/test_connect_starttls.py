import unittest
from test import support
from test.support import import_helper
from test.support import socket_helper
import smtplib
import socket
import test_smtpnet

def test_connect_starttls():
    support.get_attribute(smtplib, 'SMTP_SSL')
    context = test_smtpnet.ssl.SSLContext(test_smtpnet.ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = test_smtpnet.ssl.CERT_NONE
    with socket_helper.transient_internet(SmtpTest.testServer):
        server = smtplib.SMTP(SmtpTest.testServer, SmtpTest.remotePort)
        try:
            server.starttls(context=context)
        except smtplib.SMTPException as e:
            if e.args[0] == 'STARTTLS extension not supported by server.':
                unittest.skip(e.args[0])
            else:
                raise
        server.ehlo()
        server.quit()

SmtpTest = test_smtpnet.SmtpTest()
test_connect_starttls()
