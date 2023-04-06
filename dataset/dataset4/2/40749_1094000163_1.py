def _getstatusoutput(cmd):
    """Return Win32 (status, output) of executing cmd
in a shell."""
    pipe = os.popen(cmd, 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text