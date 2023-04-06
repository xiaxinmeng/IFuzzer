async def main():
    task = asyncio.create_task(task_that_raise())
    while True:
        try:
            await task
        except Exception as e:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            traceback.print_exception(e)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")