
import warnings
from contextlib import redirect_stderr
from io import StringIO

sio = StringIO()

with redirect_stderr(sio):
    warnings.warn("Warning 'containing' single quotes")

assert " 'containing' " in sio.getvalue()
