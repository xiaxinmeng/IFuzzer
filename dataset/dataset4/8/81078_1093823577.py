list(shlex.shlex('a ; b', posix=True, punctuation_chars=True))

list(shlex.shlex('a \; b', posix=True, punctuation_chars=True))