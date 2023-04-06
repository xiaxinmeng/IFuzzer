import sys
import logging
from functools import wraps

def myExceptHook(type, value, tb):
    """ Redirect tracebacks to error log """
    import traceback
    rawreport = traceback.format_exception(type, value, tb)
    report = '\n'.join(rawreport)
    log.error(report)

sys.excepthook = myExceptHook
    
def use_my_excepthook(view):
    """ Redirect any unexpected tracebacks """ 
    @wraps(view)
    def run(*args, **kwargs):
        try:
            return view(*args, **kwargs)
        except:
            sys.excepthook(*sys.exc_info())
    return run