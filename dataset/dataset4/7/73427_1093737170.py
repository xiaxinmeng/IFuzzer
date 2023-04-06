import sys
import os

# Force the use of legacy encoding like versions of Python prior to 3.6.
sys._enablelegacywindowsfsencoding()

# Show actual file system encoding
encoding = sys.getfilesystemencoding()
print('File system encoding:', encoding)