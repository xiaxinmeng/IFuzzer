tasks = [...]
for t in tasks:
    t.cancel()
results = await asyncio.gather(*tasks, return_exceptions=True)