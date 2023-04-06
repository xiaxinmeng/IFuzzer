
import logging

logging.basicConfig(level=logging.ERROR)

l = logging.getLogger("test")
l.setLevel(logging.DEBUG)

l.debug("Hello world")
