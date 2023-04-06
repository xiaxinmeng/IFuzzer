import logging

def setup_logging():
    # made this a function to avoid cluttering the global namespace
    logger = logging.getLogger("testlogger")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s   %(levelname)s   %(message)s')
    handler = (logging.FileHandler("testlog.log"),
               logging.StreamHandler())
    handler = handler[0] # 0 : write to logfile, 1 : write to stdout
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logging()

import m2

logger.info("Hello from %s", __name__)