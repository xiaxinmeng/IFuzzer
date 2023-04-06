async def readdev(dev):
    while True:
        buf=os.read(dev, 480)
        print([struct.unpack('llHHi', buf[i*24:(i+1)*24]) for i in range(len(buf)//24)])
        await asyncio.sleep(0)