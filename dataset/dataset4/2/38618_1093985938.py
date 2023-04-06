import ftplib
 
def transferFile(listLine):
    filename = listLine.split()[-1]
    if filename == 'README':
        # Note that retrlines uses a default
        # callback that just prints the file
        f.retrlines('RETR README') # <-- Fails
 
f=ftplib.FTP('ftp.python.org', 'ftp', 'anon@')
f.cwd('/pub/python')
f.retrlines('LIST', transferFile)
f.close()