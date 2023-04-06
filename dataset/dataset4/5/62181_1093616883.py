import logging
import logging.handlers
import daemon

logger = logging.getLogger('twitterCounter')
handler = logging.handlers.SysLogHandler(address='/dev/log')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info("Hello, ")

with daemon.DaemonContext(files_preserve=[handler.socket.fileno()]):
    logger.info("world!")