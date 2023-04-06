# vi logtest.py
import logging
import logging.handlers

logging.basicConfig(filename="test.log", level=logging.INFO)
logger = logging.getLogger("test_logger")
log_handler = logging.handlers.TimedRotatingFileHandler("test.log", when='D', backupCount=2)
logger.addHandler(log_handler)

for i in range(0, 10000):
    logger.info("iteration: %d", i)