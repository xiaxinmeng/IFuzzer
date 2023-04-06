import asyncio

e = KeyboardInterrupt  # or SystemExit


async def main_task():
    try:
        r = await asyncio.gather(sub_task(), asyncio.sleep(1))

    except (SystemExit, KeyboardInterrupt):
        # cancel current task
        asyncio.current_task().cancel()
        # give time to other tasks to run (including me)
        await asyncio.sleep(0)
        print('never reach here')
        raise
    except:
        print('')
        raise


async def sub_task():
    raise e


if __name__ == '__main__':
    try:
        asyncio.run(main_task())
    except e:
        print(f'Handle {e}')
