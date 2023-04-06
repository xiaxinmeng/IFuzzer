async with main():
    with TelegramClient('anon', api_id, api_hash) as client:
        await client.send_message('me', 'Hello, myself!')