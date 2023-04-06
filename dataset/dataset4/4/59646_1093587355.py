name = b'\xe7w\xf0'
if sys.platform == 'win32':
  try:
    os.fsdecode(name)
  except UnicodeDecodeError:
    self.skipTest("the filename %a is not decodable from the ANSI code page (%s)" % (name, sys.getfilesystemencoding()))