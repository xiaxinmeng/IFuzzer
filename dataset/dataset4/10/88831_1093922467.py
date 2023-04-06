running_tasks = set()
# [...]
task = asyncio.create_task(some_background_function())
running_tasks.add(task)
task.add_done_callback(lambda t: running_tasks.remove(t))