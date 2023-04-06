import logging
import logging.handlers
import socket

logger = logging.getLogger('mylogger')
handler = logging.handlers.SysLogHandler(('****', logging.handlers.SYSLOG_TCP_PORT), socktype=socket.SOCK_STREAM)
formatter = logging.Formatter('%(name)s: [%(levelname)s] %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("TEST 1")
logger.info("TEST 2")