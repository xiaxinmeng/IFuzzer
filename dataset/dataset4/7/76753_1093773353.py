class FTP(ftplib.FTP):
    externalip = None

    def sendport(self, host, port):
        return super().sendport(self.externalip or host, port)

    def sendeprt(self, host, port):
        return super().sendeprt(self.externalip or host, port)