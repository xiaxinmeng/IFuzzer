import sys

error = None
try:
    raise ValueError('some text')
except ValueError as err:
    error = err

if error:
    sys.exit(error)