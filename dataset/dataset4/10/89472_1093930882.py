import asyncio
import struct
counter = 0
async def on_connection(r: asyncio.StreamReader, w: asyncio.StreamWriter):
    msg = struct.pack("HB", 3, 0)
    w.write(msg)
    await w.drain()
    global counter
    counter += 1
    print(counter, "client")
async def main():
    server = await asyncio.start_server(on_connection, '0.0.0.0', 12345)
    await server.serve_forever()
if __name__ == "__main__":
    asyncio.run(main())