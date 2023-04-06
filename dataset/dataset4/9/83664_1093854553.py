import asyncio


class Singleton:
    _LOCK = None
    _LOOP = None