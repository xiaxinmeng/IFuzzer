#send the message
server.starttls()
server.login(fromaddr, p)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()