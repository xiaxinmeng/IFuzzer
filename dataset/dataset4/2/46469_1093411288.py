import logging
logging.basicConfig(filename="logtest.txt")
logging.warning("This is a test")
logging.shutdown()
logging.basicConfig(filename="logtest2.txt")
logging.warning("This is a test (2)")
logging.shutdown()