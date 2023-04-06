@dataclass
class FtpHelper(ftplib.FTP):
    my_host: str
    my_user: str
    lookup_password: InitVar[Callable]

    def __post_init__(self, lookup_password):
        super().__init__(host=self.my_host, user=self.my_user, passwd=lookup_password())

def get_password():
    return "a password"

ftp = FtpHelper(hostname, username, get_password)