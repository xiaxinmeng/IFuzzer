ready_tasks = []
while True:
    # The usual asyncio behaviour
    task = ready_tasks.pop(0)
    task.run()

    # Run down dependency chain until we hit a task with next_task == None
    # In this case, next_task would be the return to wait_for
    while task.next_task:
        task = task.next_task
        task.run()
        # Cleanup tasks list needed here