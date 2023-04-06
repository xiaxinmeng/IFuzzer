f = file('somemessage')
import email
m = email.message_from_file(f)
f2 = file('newmsg', 'w')
f2.write(m.as_string())