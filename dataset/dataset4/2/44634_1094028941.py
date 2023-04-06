import email
print (email.message_from_file(open("test5.eml")).as_string(False))