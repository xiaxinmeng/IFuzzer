def getfile(ftpobj, filename, callback=[]):
    'This code works before the patch, but not after'
    ftpobj.retrlines('retr '+filename, callback)