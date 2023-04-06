# Exceptions which must not call the exception handler in fatal error
# methods (_fatal_error())
_FATAL_ERROR_IGNORE = (BrokenPipeError, ConnectionResetError, ConnectionAbortedError)