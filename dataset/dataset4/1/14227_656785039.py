async def consumer(queue):
    while not_done:
      job = await queue.get()
      result = await do_stuff(job)

async def producer(queue):
    while not_done:
      job = await make_job()
      await queue.put(job)