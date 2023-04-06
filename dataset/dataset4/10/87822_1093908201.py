class TriggerTracebackBug:
    _repr = None
    def __init__(self):
        raise RuntimeError("can't build a TriggerTracebackBug object for some reason")
        self._repr = 'if we reached this line, this object would have a repr result'
    def __repr__(self):
        return f'<Myclass: {self._repr}>'