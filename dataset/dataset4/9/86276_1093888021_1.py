# Patch os.kill to call sleep(1) first,
# opening up the window for a race condition
os_kill = os.kill
def kill(p, n):
    time.sleep(1)
    os_kill(p, n)

os.kill = kill

async def main():
    p = await asyncio.create_subprocess_exec(sys.executable, '-c', 'import sys; sys.exit(0)')
    p.send_signal(signal.SIGTERM)
    # cleanup
    await p.wait()

asyncio.run(main())