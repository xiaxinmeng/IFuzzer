##############################
# example1.py
from asyncio import BaseEventLoop  # Module 'asyncio' has no attribute 'BaseEventLoop'
from asyncio import Semaphore  # OK
import aiostream  # gets skipped correctly
import asyncio  # OK
asyncio.windows_events.WindowsProactorEventLoopPolicy()  # Module has no attribute 'windows_events'
asyncio.WindowsProactorEventLoopPolicy()  # Module has no attribute 'WindowsProactorEventLoopPolicy'