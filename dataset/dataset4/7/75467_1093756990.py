def import_in_finally_fail():
    try:
        print('yo')
    finally:
        import asyncio.queues as aq