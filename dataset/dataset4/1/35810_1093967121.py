# Really ugly hack; don't try this at home:
def ftpwrapper_init(self):
    import ftplib
    self.busy = 0
    self.ftp = ftplib.FTP()
    self.ftp.set_pasv(1)
    self.ftp.connect(self.host, self.port)
    self.ftp.login(self.user, self.passwd)
    for dir in self.dirs:
        self.ftp.cwd(dir)

urllib.ftpwrapper.init = ftpwrapper_init
# End really ugly hack