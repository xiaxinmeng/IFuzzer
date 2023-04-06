fileTest = open('filename1', 'wb')

ftp.retrlines('RETR README.html', fileTest.write)