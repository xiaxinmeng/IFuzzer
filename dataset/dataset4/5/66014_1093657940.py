imaplib.Debug = 5
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password) # Enter your login here
mail.select('test')