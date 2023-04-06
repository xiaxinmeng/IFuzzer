import asyncio

@asyncio.coroutine
def SomeCoroutine():
    print("test...")

@asyncio.coroutine
def SomeNormalFunction():
    SomeCoroutine()