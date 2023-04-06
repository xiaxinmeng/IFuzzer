
async def main():
    async for i in double(count()):
        if i > 10:
            break
        print(i)
    await asyncio.sleep(0)
