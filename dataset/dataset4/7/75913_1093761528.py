logger.debug("Oops: something bad happened! %s", exc)
for line in my_exception_formatter(exc):
   logger.trace(line)