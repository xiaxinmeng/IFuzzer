from __future__ import unicode_literals

import io
import sys
import traceback

PY3 = sys.version_info > (3,)

print(sys.version)

buffer = io.StringIO() if PY3 else io.BytesIO()