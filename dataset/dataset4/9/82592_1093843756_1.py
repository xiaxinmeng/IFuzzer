attempts = 0

while True:
    attempts += 1
    if asyncio.run(misuse_sqlite()):
        print('error hit on attempt', attempts)
        break