import sys
import asyncio


async def run_subprocess():
    proc = await asyncio.create_subprocess_shell(
        "exit 0",
        stdin=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    await proc.wait()
    print("success!")


async def amain():
    await asyncio.to_thread(asyncio.run, run_subprocess())


def main():
    asyncio.get_event_loop_policy().set_child_watcher(asyncio.SafeChildWatcher())
    asyncio.run(amain())


if __name__ == "__main__":
    sys.exit(main())