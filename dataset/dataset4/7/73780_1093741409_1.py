class LogLevel(Flags):
     start = auto()
     _log1 = auto()
     log1 = start | _log1
     _log2 = auto()
     log2 = start | _log2