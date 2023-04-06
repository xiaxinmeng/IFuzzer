def init(self):
    import ftplib
    self.busy = 0
    self.ftp = ftplib.FTP()
    self.ftp.connect(self.host, self.port, self.timeout)
    self.ftp.login(self.user, self.passwd)
    _target = '/'.join(self.dirs)
    self.ftp.cwd(_target)