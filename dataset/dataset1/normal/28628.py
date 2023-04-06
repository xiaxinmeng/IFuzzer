#!/usr/bin/env python3

import signal
import asyncio

def foo():
    pass

async def bar():
    pass

def main():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, lambda: None)
    loop.add_signal_handler(signal.SIGHUP, lambda: None)
    loop.run_until_complete(bar())


if __name__ == "__main__":
    main()
