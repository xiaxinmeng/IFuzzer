async def main():
  loop = asyncio.get_running_loop()
  loop.set_exception_handler(...)
  # other code

asyncio.run(main())