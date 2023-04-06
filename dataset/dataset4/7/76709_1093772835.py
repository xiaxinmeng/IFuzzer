async def xxxx():
    while True:
        try:
            result = await download()
            handle_result(result)
        except Exception as e:
            log.warning('Fail..%r', e)
        await asyncio.sleep()