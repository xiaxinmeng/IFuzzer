async def forward_stream(reader: StreamReader, writer: StreamWriter, event: asyncio.Event, source: str):
    writer_drain = writer.drain()
    while not event.is_set():
        try:
            data = await asyncio.wait_for(reader.read(1024), 1)
        except asyncio.TimeoutError:
            continue

        if not data:
            event.set()
            break

        # parse the data
        if reading := parse(data):
            # wait for the previous write to finish, and forward the data to the other end, process the data in between
            await writer_drain
            writer.write(data)
        writer_drain = writer.drain()