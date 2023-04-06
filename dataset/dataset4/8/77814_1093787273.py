msg = MIMEText("The report at *link* has been updated")
for recipient in recipient_list:
    msg['To'] = recipient_email
    server.sendmail(from_address, recipient_email, msg.as_string())