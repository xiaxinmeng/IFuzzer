import asyncio
import logging


def handle_exception(loop, context):
    msg = context.get("exception", context["message"])
    logging.error("Caught exception: %s", msg)

async def test():
    await asyncio.sleep(1)
    raise Exception("Crash.")

def main():
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_exception)
    # if removed "task = " - exception handler will work.
    task = loop.create_task(test())
    try:
        loop.run_forever()
    finally:
        loop.close()


if __name__ == "__main__":
    main()