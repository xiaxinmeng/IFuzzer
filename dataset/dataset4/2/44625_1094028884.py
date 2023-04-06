#!/usr/bin/env python
import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
format = "%(levelname)-8s %(module)s %(lineno)d %(message)s"
handler.setFormatter(logging.Formatter(format))
logger.addHandler(handler)

logger.info("Yo")