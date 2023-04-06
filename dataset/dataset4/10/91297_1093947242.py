from email.message import EmailMessage

nested_message = EmailMessage()
nested_message.set_content("Gazpacho!")

env = EmailMessage()
env.add_header("Content-Type", "multipart/signed", protocol="application/pkcs7-signature", micalg='sha-256')
env.preamble = "This is an S/MIME signed message"
env.attach(nested_message)
print(str(env))