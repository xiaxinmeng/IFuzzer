
import asyncio

def the_answer():
	return 42

async def the_answer2():
	await asyncio.sleep(100)
	return the_answer()
