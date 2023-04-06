import smtplib

a = smtplib.SMTP_SSL('gmail-smtp-in.l.google.com.')
a.starttls()

a = smtplib.SMTP_SSL('mail.internode.on.net')
a = smtplib.SMTP_SSL('smtp.gmail.com')

import ftplib
# http://secureftp-test.com/

f = ftplib.FTP_TLS('ftp.secureftp-test.com')
f.auth()

import imaplib
i = imaplib.IMAP4('calmail.berkley.edu')
i.starttls()

i = imaplib.IMAP4_SSL('mail.internode.on.net')

import poplib

p = poplib.POP3_SSL('calmail.berkley.edu')

import  nntplib 
n = nntplib.NNTP_SSL('news.internode.on.net')