def putcmd(self, cmd, args=""):
    """Send a command to the server."""
    if args == "":
        str = '%s%s' % (cmd, CRLF)
    else:
        str = '%s %s%s' % (cmd, args, CRLF)
    self.send(str)