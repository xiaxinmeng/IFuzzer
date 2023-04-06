import email.message
mail = email.message.EmailMessage()
mail.add_attachment(b"test", maintype="text", subtype="plain", filename="é.txt")
print(mail)