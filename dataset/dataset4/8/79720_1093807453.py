async def test():
    proc = await asyncio.create_subprocess_shell(
        "sleep 1", stdout=asyncio.subprocess.PIPE)
    proc.terminate()
    await proc.wait()