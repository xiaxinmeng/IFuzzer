async def postgres():
    import aiopg
    async with aiopg.create_pool('') as pool:
        async with pool.acquire() as connection:
            connection._notifies = MyQueue()
            async with connection.cursor() as cursor:
                await cursor.execute('LISTEN message')
                async for message in connection.notifies:
                    for ws in ws_set: await ws.send(message.payload)