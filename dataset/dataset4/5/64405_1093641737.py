# coding=utf-8
import email
import email.charset
import email.message

c = email.charset.Charset('utf-8')
c.body_encoding = email.charset.QP
m = email.message.Message()
m.set_payload("This is a Greek letter upsilon: υ", c)
print(m.as_string())