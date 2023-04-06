
from concurrent.futures import ProcessPoolExecutor
import asyncio
import os
import signal
import sys
import time


def background_task():
    print(f"Running background task {os.getpid()}", file=sys.stderr)
    time.sleep(15)
    print("Exiting background task", file=sys.stderr)


async def task():
    print("Running task")

    executor = ProcessPoolExecutor()
    with executor:
        loop = asyncio.get_event_loop()

        try:
            await loop.run_in_executor(executor, background_task)
        except asyncio.CancelledError:
            print("Cancelling task 1", file=sys.stderr)

            try:
                await asyncio.sleep(15)
            except asyncio.CancelledError:
                print("Cancelling task 2", file=sys.stderr)
                raise

            raise

def main():
    def terminate(coro):
        print(f"Terminating {os.getpid()}")
        coro.cancel()

    loop = asyncio.get_event_loop()
    t = asyncio.ensure_future(task())
    loop.add_signal_handler(signal.SIGTERM, terminate, t)

    try:
        print(f"Running {os.getpid()}", file=sys.stderr)
        loop.run_until_complete(t)
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    main()
