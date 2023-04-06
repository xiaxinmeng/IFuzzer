
import asyncio
import sys


async def read_stdin():
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await asyncio.get_running_loop().connect_read_pipe(lambda: protocol, sys.stdin)
    while True:
        line = await reader.readline()
        print("stdin > ", line)


async def main():
    task = asyncio.create_task(read_stdin())
    await asyncio.sleep(5)
    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
