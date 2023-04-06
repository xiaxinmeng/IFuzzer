await create_task(not_coro())
await ensure_future(not_coro())
await gather(not_coro())
await wait([not_coro()])
await wait([not_coro()])
await wait_for(not_coro(), 10)
await shield(not_coro())

for f in as_completed([not_coro()]):
    print(await f)