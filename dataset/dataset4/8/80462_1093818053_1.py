
import pexpect
import sys

child = pexpect.spawn("python /Users/basnijholt/Downloads/cpython/test.py")
try:
    child.expect(["OSError", "AssertionError"], timeout=1)
    raise Exception
except pexpect.EOF as e:
    sys.exit(0)
