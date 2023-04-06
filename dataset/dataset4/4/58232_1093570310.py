class NoStackTraceFormatter(logging.Formatter):
    def formatException(self, exc_info):  # Don't emit the stack trace
        return '\n'.join(traceback.format_exception_only(exc_info[0], exc_info[1])) # type and value only

    def format(self, record):
        saved_exc_text = record.exc_text # optional
        record.exc_text = None
        result = super(NoStackTraceFormatter, self).format(record)
        record.exc_text = saved_exc_text # or None, if you want
        return result