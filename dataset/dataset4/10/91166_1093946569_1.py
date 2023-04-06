async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)