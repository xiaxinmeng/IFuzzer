import os
open('foo', 'wb').close()
flags = os.O_RDWR | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_BINARY', 0)
os.open('foo/bar', flags, 0o600)          # what raised?
os.open('nonexistent/bar', flags, 0o600)  # what raised?