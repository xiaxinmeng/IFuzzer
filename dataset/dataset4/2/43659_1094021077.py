if aol:
    auths = [smtplib.AUTH_CRAM_MD5, smtplib.AUTH_LOGIN,
smtplib.AUTH_PLAIN]
    smtp.login(fromUser.split("@")[0], passwd, auths)
else:
    smtp.login(fromUser, passwd)