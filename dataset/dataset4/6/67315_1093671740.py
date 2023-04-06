def try_import(n):
    try: return __import__(n)
    except ImportError: raise NameError("Name %r is not defined"%n)

import sys
sys.__getglobal__ = try_import