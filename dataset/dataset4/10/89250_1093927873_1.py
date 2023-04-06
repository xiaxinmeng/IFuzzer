message = 'Python is fun'
byte_message = bytes(message, 'utf-8')
print(byte_message)
#byte_message.split(",") causes error
str(byte_message).split(",") # works