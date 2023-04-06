async def main_task():
    try:
        await asyncio.gather(
            sub_task(),
            asyncio.sleep(0)
        )
    except Exception as e:
        raise
   
    except BaseException as e:
        print(repr(e))