
import asyncio
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


async def method_that_raises():
    loop = asyncio.get_event_loop()
    try:
        logger.info("raising exception")
        raise ValueError("my exception1")
    # except Exception as e:
    #     logger.info("in catcher")
    #     logger.exception(e)
    #     raise
    finally:
        logger.info("stopped")
        loop.stop()
        # await asyncio.sleep(0.5)

        return


async def another_level():
    try:
        await method_that_raises()
    except Exception as e:
        logger.info("trapping from another_level")
        logger.exception(e)


if __name__ == "__main__":
    logger.info("start")
    try:
        asyncio.run(another_level())
    except Exception as e:
        logger.exception(e)
    logger.info("done")
