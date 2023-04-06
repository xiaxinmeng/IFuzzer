import email.message
mail = email.message.EmailMessage()
mail.add_attachment(
   b"test",
   maintype = "text",
   subtype  = "plain",
   filename = "I thought I could put a few words in the filename but apparently it does not go so well.txt" 
)
print(mail)