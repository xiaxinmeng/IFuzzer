import asyncio
import concurrent
import threading


def prepare_a_giant_list():
    m = []
    for i in range(1000*1000):
        m.append("There's a fat fox jump over a sheep" + str(i))

    th_num = threading.active_count()
    print("Thread number is {}".format(th_num))
    return m


async def main():
    loop = asyncio.get_running_loop()
    async_executor = concurrent.futures.ThreadPoolExecutor(max_workers=20)
    await loop.run_in_executor(async_executor, prepare_a_giant_list)
    await asyncio.sleep(15)
    await loop.run_in_executor(async_executor, prepare_a_giant_list)
    await asyncio.sleep(15)
    await loop.run_in_executor(async_executor, prepare_a_giant_list)
    await asyncio.sleep(15)
    await loop.run_in_executor(async_executor, prepare_a_giant_list)
    await asyncio.sleep(15)


if __name__ == "__main__":
    asyncio.run(main())