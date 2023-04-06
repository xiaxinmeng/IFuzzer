
import asyncio

class it:
	async def __aenter__(self):
		return self
	async def __aexit__(self, *_):
		print('EXIT')

async def main():
	async with it():
		await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
