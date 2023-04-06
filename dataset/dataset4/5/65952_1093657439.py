def list2shellcmd(seq):
    """Turn the sequence of arguments into a single command line, with escaped characters."""
    if mswindows:
        line=list2cmdline(seq).replace("^", "^^")
    else:
        line=" ".join(seq)
    return line