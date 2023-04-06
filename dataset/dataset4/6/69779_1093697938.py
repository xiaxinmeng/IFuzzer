import asyncio

loop = asyncio.get_event_loop()

def batch_open():
    for i in range(100):
        c = asyncio.ensure_future(asyncio.open_connection('127.0.0.1', 8080))
        c.add_done_callback(on_resp)

def on_resp(task):
    task.result()
    loop.stop()

loop.call_soon(batch_open)
while True:
    loop.run_forever()