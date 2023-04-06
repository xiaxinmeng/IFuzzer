
async def main():
    """Cancel a gather() future and child and return it."""
    task_child = ensure_future(sleep(1.0))
    future_gather = gather(task_child)

    task_child.cancel()
    try:
        await future_gather
    except asyncio.CancelledError:
        pass

    return future_gather, task_child
