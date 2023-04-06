fp = s.makefile('r')
fp.read()
fp.close()
s.close()

#ftplib falsely sees "226 transfer complete" as response to next command
ftp.sendcmd('NOOP')