
import asyncio
import ssl
import certifi

hostname = 'login.microsoftonline.com'
context = ssl.create_default_context()
context.load_verify_locations(cafile=certifi.where())

async def main():
    reader, writer = await asyncio.open_connection(hostname, 443, ssl=context)
    print('opened')
    writer.close()
    print('close started')
    await writer.wait_closed()
    print('close completed')

asyncio.run(main())
