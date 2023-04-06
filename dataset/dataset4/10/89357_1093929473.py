async def test_task():
    while True:
        ts_now = time.time();
        await asyncio.sleep(1.000);
        print("{}".format((time.time()-ts_now)*1000.0));

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(thread_main())
    loop.run_forever()