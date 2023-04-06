def getstatus(cmd):
    """Return exit status of executing cmd in a
shell."""
    return getstatusoutput(cmd)[0]