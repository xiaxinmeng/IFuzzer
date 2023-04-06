loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.create_subprocess_exec('/doesntexist'))
except FileNotFoundError:
    pass
finally:
    loop.close()