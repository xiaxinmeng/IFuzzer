async with asyncio.timeout(1):
    try:
        await asyncio.sleep(2)  # Will be cancelled by the timeout
    finally:
        1/0  # oops, crash in cleanup