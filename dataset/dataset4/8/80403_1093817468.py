async def main():
    await asyncio.gather(mocked_function())

asyncio.run(main())