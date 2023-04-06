
import asyncio
import functools
import os
import signal


def ask_exit(signame):

    print("\n[ask_exit] got signal %s: exit" % signame)
    try:
        asyncio.get_running_loop().stop()
    except Exception as e:
        print(f'[ask_exit] Exception: {e}')
    finally:
        print(f'[ask_exit] {signame} completed')


async def main():
    loop = asyncio.get_running_loop()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(
            getattr(signal, signame),
            functools.partial(ask_exit, signame))

    print(f'[main] signal handlers added; begin sleep')
    await asyncio.sleep(3600) # sleep until time elapses


print(f"[INFO] Event loop will run and sleep for 1 hour. Press Ctrl+C to interrupt its sleep.")
print(f"[INFO] pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

try:
    asyncio.run(main())
except Exception as e:
    print(f'[INFO] {e}')
finally:
    print(f'[INFO] program is done')
