async def solve_iteratively(initial_x, next_approximation):
    result = initial_x
    try:
        while True:
            result = next_approximation(result)
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        return result