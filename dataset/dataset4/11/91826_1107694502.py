
import ssl
ssl_context = ssl.create_default_context()
assert ssl_context.check_hostname is True

from functools import partial, partialmethod
import ftplib, imaplib, nntplib, poplib, smtplib, xmlrpc.client
ftplib.FTP_TLS = partial(ftplib.FTP_TLS, context=ssl_context)
imaplib.IMAP4_SSL = partial(imaplib.IMAP4_SSL, ssl_context=ssl_context)
imaplib.IMAP4.starttls = partialmethod(imaplib.IMAP4.starttls, ssl_context=ssl_context)
nntplib.NNTP_SSL = partial(nntplib.NNTP_SSL, ssl_context=ssl_context)  # note: deprecated library
nntplib.NNTP.starttls = partialmethod(nntplib.NNTP.starttls, context=ssl_context)  # ditto
poplib.POP3_SSL = partial(poplib.POP3_SSL, context=ssl_context)
poplib.POP3.stls = partialmethod(poplib.POP3.stls, context=ssl_context)
smtplib.SMTP_SSL = partial(smtplib.SMTP_SSL, context=ssl_context)
smtplib.SMTP.starttls = partialmethod(smtplib.SMTP.starttls, context=ssl_context)
xmlrpc.client.ServerProxy = partial(xmlrpc.client.ServerProxy, context=ssl_context)
del ssl_context, ssl, partial, partialmethod
