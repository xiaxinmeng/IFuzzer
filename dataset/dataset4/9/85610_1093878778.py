
import asyncio
from concurrent import futures


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s %(name)s %(levelname)s]: %(message)s",
    datefmt="%H:%M:%S %d-%m-%y",
)
logger: logging.Logger = logging.getLogger("ideahitme")


async def too_long() -> None:
    await asyncio.sleep(2)


async def run() -> None:
    try:
        await asyncio.wait_for(too_long(), 1)
    except futures.TimeoutError:
        logger.info("concurrent.futures.TimeoutError happened")
    except asyncio.TimeoutError:
        logger.info("asyncio.TimeoutError happened")


if __name__ == "__main__":
    asyncio.run(run())
