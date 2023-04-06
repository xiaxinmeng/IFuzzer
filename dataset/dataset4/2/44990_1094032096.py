def split(s, comments=False, posix=True):
    lex = shlex(s, posix)
    lex.whitespace_split = True
    if not comments:
        lex.commenters = ''
    return list(lex)