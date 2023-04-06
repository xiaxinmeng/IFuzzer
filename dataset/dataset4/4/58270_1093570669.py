def sendMail (fromAddr, toAddr, subject, body = '', attachment = ''):
    message = email.mime.multipart.MIMEMultipart()
    message.add_header('From',fromAddr)
    message.add_header('To',toAddr)