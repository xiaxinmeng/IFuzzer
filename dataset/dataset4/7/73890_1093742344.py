import asyncio

async def execute():
    process = await asyncio.create_subprocess_exec(
        "timeout", "0.1", "cat", "/dev/urandom", stdout=asyncio.subprocess.PIPE)

    while True:
        data = await process.stdout.read(65536)
        print('read %d bytes' % len(data))
        if data:
            await asyncio.sleep(0.3)
        else:
            break