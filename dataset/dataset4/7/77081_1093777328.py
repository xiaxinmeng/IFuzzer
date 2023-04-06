async def foo():
    import pdb;pdb.set_trace()
    async with gen() as x:
        assert x == 1234
    print("done")

trio.run(foo)
# asyncio.get_event_loop().run_until_complete(foo())