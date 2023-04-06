DATE = datetime.datetime.utcnow().strftime('%m/%d/%Y %I:%M:%S %p')
msg['Date'] = datetime.datetime.utcnow().strftime('%m/%d/%Y %I:%M:%S %p')

server= smtplib.SMTP("igpm.igpm.rwth-aachen.de")
# server= smtplib.SMTP('relay.skynet.be')
server.set_debuglevel(9)

msg.set_payload("Gedanken über einen Test","iso-8859-1")
# server.send_message(msg)
server.sendmail(FromAddr,ToAddr,msg.as_string().encode("iso-8859-1"))
server.quit()