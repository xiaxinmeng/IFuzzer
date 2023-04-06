import shlex
list(shlex.shlex('foo,bar', punctuation_chars=True))
