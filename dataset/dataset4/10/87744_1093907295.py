
import asyncio
import signal

async def main():
    while True:
        proc = await asyncio.create_subprocess_exec('sleep', '0.1')
        await asyncio.sleep(0.1)
        try:
            proc.send_signal(signal.SIGUSR1)
        except ProcessLookupError:
            pass
        assert (await proc.wait() != 255)

asyncio.run(main())

