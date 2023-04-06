def redirect_stdout(replacement=None):
  return unittest.mock.patch('sys.stdout', replacement if replacement is not None else io.StringIO())