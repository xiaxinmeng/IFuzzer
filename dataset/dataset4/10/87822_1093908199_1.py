import traceback
class TriggerTracebackBug:
    def __init__(self):
        raise RuntimeError("can't build a TriggerTracebackBug object for some reason")
        self._repr = 'if we reached this line, this object would have a repr result'
    def __repr__(self):
        return self._repr
try:
    TriggerTracebackBug()
except Exception as e:
    # this method call fails because there is a stack frame with a local
    # variable (self) such that repr fails on that variable's value:
    traceback.TracebackException.from_exception(e, capture_locals=True)