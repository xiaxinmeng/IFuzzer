async def get_data():
    cursor.execute('select * from stuff')
    async for row in AsyncIteratorWrapper(cursor):
        process(row)