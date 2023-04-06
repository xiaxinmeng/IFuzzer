def sig_interrupt():
    print('interrupt')
    for task in asyncio.Task.all_tasks():
        task.cancel()

loop.add_signal_handler(signal.SIGINT, sig_interrupt)
...