import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('username@gmail.com', 'password') # Enter your login here
mail.select('test') # Mailbox selection. I have a test inbox with 6
                    # messages in it.
code, [msg_ids] = mail.search(None, 'ALL')
first_id = msg_ids.split()[0]
mail.store(first_id, "+FLAGS", "[test]")
typ, response = mail.fetch(first_id, '(FLAGS)')
print("Flags: %s" % response)
mail.close()
mail.logout()