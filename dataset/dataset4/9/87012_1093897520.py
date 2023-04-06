import test.support
import sys

import _testcapi

print(f"{sys.stdout.encoding=}", file=sys.stderr)

with test.support.SuppressCrashReport():
    _testcapi.run_in_subinterp("pass")