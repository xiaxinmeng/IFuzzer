import logging
log = logging.getLogger("test")
log.addHandler(logging.FileHandler("log.out"))
log.warning("foo\x80")