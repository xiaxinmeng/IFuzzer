
import sys
assert sys.stdout.isatty()
print("stdout encodingg:", sys.stdout.encoding)
reopen_stdout = open(sys.stdout.fileno(), closefd=False)
print("reopen encoding:", reopen_stdout.encoding)
reopen_stdout.close()
