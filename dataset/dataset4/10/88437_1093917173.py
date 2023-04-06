import asyncio
import timeit

num = 0


async def test():
    global num
    num += 1
    print(f"done task {num}")
    return f"task: {num}"


async def main():
    task = asyncio.create_task(test())