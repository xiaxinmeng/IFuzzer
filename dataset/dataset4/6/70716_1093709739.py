# Set transfer mode to ASCII!
self.ftp.voidcmd('TYPE A')
# Try a directory listing. Verify that directory exists.
if file:
    pwd = self.ftp.pwd()
    try:
        try:
            self.ftp.cwd(file)
        except ftplib.error_perm as reason:
            raise URLError('ftp error: %r' % reason) from reason
    finally:
        self.ftp.cwd(pwd)
    cmd = 'LIST ' + file
else:
    cmd = 'LIST'
conn, retrlen = self.ftp.ntransfercmd(cmd)