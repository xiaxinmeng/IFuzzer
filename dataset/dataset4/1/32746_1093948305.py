e = sys.stderr.write
w = sys.stdout.write

e(400*'this is a test\n')
posix.close(2)
w(400*'this is another test\n')