for s in '\x0a\x0d\x1c\x1d\x1e':
  print('a{}b'.format(s).splitlines(1),
        bytes('a{}b'.format(s), 'utf-8').splitlines(1))