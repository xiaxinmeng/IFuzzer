f = open("memleak.eml")
buffer = f.read()
f.close()

# now buffer has the email string
msg = email.message_from_string(buffer)
msg = None # this should free the memory but it doesn't