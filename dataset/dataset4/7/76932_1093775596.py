async with aclosing(agen):
    await wait_for(agen.asend(...), timeout=...)