parser = make_parser()
parser.parse(path)

# This unlink fails on win32.  It succeeds if I comment out the call to parse.
os.unlink(path)