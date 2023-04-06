
import asyncio


class Singleton:
    _CREATE_LOCK = asyncio.Lock()

    @classmethod
    async def create(cls):
        if not hasattr(cls, '_Singleton__instance'):
            async with cls._CREATE_LOCK:
                if not hasattr(cls, '_Singleton__instance'):
                    await asyncio.sleep(1)
                    cls.__instance = cls()
        return cls.__instance


async def main():
    await asyncio.wait([
        Singleton.create(),
        Singleton.create(),
    ])


if __name__ == '__main__':
    asyncio.run(main())
