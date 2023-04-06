c = self.rawq_getchar()
...
if c == IAC:
  buf = buf + c
elif c in (DO, DONT):
  opt = self.rawq_getchar()
  ...
elif  c in (WILL, WONT):
  opt = self.rawq_getchar()
  ...
else:
  self.msg('IAC %d not recognized' % ord(opt))