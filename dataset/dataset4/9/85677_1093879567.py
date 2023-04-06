
async def do(n: int) -> None:
    print('running', n)
    await asyncio.sleep(1)
    print('returning', n)
    return n

async def main():
    result = []
    async for x in materialize(map(do, range(5)), max_concurrency=2):
        print('got', x)
        result.append(x)

    print(result)
