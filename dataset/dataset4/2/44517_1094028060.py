import sys, logging
logger = logging.getLogger("cookielib")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)