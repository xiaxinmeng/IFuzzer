from ftplib import FTP
ftp = FTP('ftp.unicamp.br')
ftp.login()
ftp.cwd('pub/libreoffice') # throws error
ftp.cwd('pub/libreoffice/') # OK