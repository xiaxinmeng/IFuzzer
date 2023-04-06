import asyncio
import logging

logging.basicConfig()

logger = asyncio.log.logger
output = open("asyncio.log", "a")
handler = logging.StreamHandler(output)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

asyncio.log.logger.debug("plop")
output.close()