import logging.config
import socket
from logging.handlers import SysLogHandler

log = logging.getLogger("logtest")
syslog_handler = SysLogHandler(("127.0.0.1", 12345), socktype=socket.SOCK_DGRAM)
log.addHandler(syslog_handler)

log.warning("Works")

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
    }
)

log.warning("Breaks")