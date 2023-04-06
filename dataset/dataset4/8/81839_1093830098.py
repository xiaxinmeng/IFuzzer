
async def create_connection(ssl_obj):
    loop = asyncio.get_event_loop()
    connector = loop.create_connection(MyEchoClientProtocol, '127.0.0.1', 5000, ssl=ssl_obj)
    connector = asyncio.ensure_future(connector)
    try:
        tr, pr = await connector
    except asyncio.CancelledError:
        if connector.done():
            tr, pr = connector.result()
            # Uncommenting the following line fixes the problem:
            # tr.close()
        raise
    return tr, pr
