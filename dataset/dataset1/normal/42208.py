import logging

class A:
    def __del__(self):
        logger.error("a")

logging.basicConfig(filename="toto.txt")
logger = logging.getLogger()
a = A()
