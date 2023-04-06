async def main():
    on_con_lost = asyncio.Future()
    transport, protocol = await asyncio.get_event_loop().create_connection(
        lambda: TestProtocol(on_con_lost),
        family=socket.AF_INET6,
        flags=socket.AI_V4MAPPED,
        host='neverssl.com',
        port=80)