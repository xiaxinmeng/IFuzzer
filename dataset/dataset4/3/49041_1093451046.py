import ftplib

ftp = ftplib.FTP('ftp.edgecastcdn.net', user='theusername',
passwd='thepassword')
ftp.cwd('chrismahan-675')
ftp.dir()
#ftp.retrlines('LIST')
ftp.close()