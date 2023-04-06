async def main():
    await coro()      # ok
    await not_coro()  # will fail with TypeError: object generator can't be used in 'await' expression