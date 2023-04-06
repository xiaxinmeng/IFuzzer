@dataclass
class FtpHelper(ftplib.FTP):
    host: str
    baz: str