import sys

# Force the use of legacy encoding like versions of Python prior to 3.6.
sys._enablelegacywindowsfsencoding()

# Show actual file system encoding
encoding = sys.getfilesystemencoding()
print('File system encoding:', encoding)

# os.fsencode(filename) VS filename.encode(File system encoding)
import os
print(os.fsencode('é'), 'é'.encode(encoding))