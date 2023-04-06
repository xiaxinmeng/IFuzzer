ftp = FTP('ftp.cdrom.com')
ftp.login('anonymous', 'anonymous@')
ftp.retrlines('LIST')