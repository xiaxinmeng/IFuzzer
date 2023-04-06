from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

import locale
print(locale.getpreferredencoding())

sys.stdout = old_stdout

print(mystdout.getvalue())