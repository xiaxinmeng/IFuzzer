with open('crap2.txt', 'w') as fp:
    ftp.retrlines('RETR crap.txt', fp.write)