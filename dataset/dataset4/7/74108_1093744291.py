import asyncio
class Test():
    async def __aenter__(self):
        print("aenter used")
        value = asyncio.Future()
        value.set_result(True)
        return value
    #FORGOT TO MARK AS async !!
    def __aexit__(self, *errors):
        print("aexit used")
        return None

async def my_test():
    async with Test() as x:
        print("inside async with, now awaiting on", x)
        await x