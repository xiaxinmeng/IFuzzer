
import asyncio

async def dwdiff():
    process = await asyncio.create_subprocess_exec(
        '/usr/local/bin/dwdiff', 'f1.txt', 'f2.txt',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await process.communicate()

async def main():
    await asyncio.gather(*(dwdiff() for __ in range(25)))

asyncio.run(main())
