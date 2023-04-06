
async def update_users(db, user):
    async with db.connection() as conn:
        async with conn.transaction() as tx:
            ...
