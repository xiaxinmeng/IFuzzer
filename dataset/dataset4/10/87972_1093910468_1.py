read_transport = None
read_stream = None

async def _connect_read(loop):
    global read_transport
    global read_stream
    stream_reader = asyncio.StreamReader()
    def protocol_factory():
        return asyncio.StreamReaderProtocol(stream_reader)
    rpipe = os.fdopen(prx, mode='r')