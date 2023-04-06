def helo(self, name=''):
    """SMTP 'helo' command.
    Hostname to send for this command defaults to the FQDN of the local
    host.
    """
    self.putcmd("helo", name or self.local_hostname)
    (code, msg) = self.getreply()
    self.helo_resp = msg
    return (code, msg)