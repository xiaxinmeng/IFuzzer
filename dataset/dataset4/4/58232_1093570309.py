class NoStackTraceFormatter(logging.Formatter):
    def formatException(self, exc_info):  # Don't emit the stack trace
        return '\n'.join(traceback.format_exception_only(exc_info[0], exc_info[1])) # type and value only