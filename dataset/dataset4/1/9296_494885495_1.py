m = AsyncMock(**{"a.return_value": "mocka", "b.return_value": "mockb"})
async def check(m):
    print(m.b())
    print(await m.a())