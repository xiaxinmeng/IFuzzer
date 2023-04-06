async def a():
    with move_on_after(5):
        await a_long_op()
    await something_else()