background_tasks = set()
def create_connection_task(*args, **kwargs):
    task = asyncio.create_task(handle_connection(*args, **kwargs))
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)

# asyncio.start_server(create_connection_task, ..)