import atexit
atexit.register(lambda: logging.info("so long"))
import logging
logging.basicConfig(filename='test.log', filemode='w', level=logging.INFO)
logging.info("super important stuff")