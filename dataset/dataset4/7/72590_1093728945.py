sHandler = logging.handlers.SysLogHandler(address=(address[0], address[1]), socktype = socket.SOCK_STREAM)
sHandler.setFormatter(logging.Formatter(fmt=MSG_SYSLOG_FORMAT, datefmt=DATE_FMT))
self.addHandler(sHandler)