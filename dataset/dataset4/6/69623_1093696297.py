import ftplib
ftp = ftplib.FTP_TLS(ftphost, ftpuser, ftppass)
ftp.prot_p()
ftp.retrbinary('RETR ' + cmofile, infile.write)