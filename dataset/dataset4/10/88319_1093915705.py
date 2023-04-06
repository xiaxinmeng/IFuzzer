
import asyncio
import sys

# Tested with:
# asyncio.ThreadedChildWatcher (3.10.0a7  only)
# asyncio.MultiLoopChildWatcher (3.10.0a7 only)
# asyncio.SafeChildWatcher (3.7.9 and 3.10.0a7)
# asyncio.FastChildWatcher (3.7.9 and 3.10.0a7)
# Not tested with asyncio.PidfdChildWatcher because I'm not on Linux.
WATCHER_CLASS = asyncio.FastChildWatcher

async def main():
    # Dummy command that should be executable cross-platform.
    process = await asyncio.subprocess.create_subprocess_exec(
        sys.executable, "--version"
    )
    
    for i in range(20):
        # I think the problem is that the event loop opportunistically wait()s
        # all outstanding subprocesses on its own. Do a bunch of separate
        # sleep() calls to give it a bunch of chances to do this, for reliable
        # reproduction.
        #
        # I'm not sure if this is strictly necessary for the problem to happen.
        # On my machine, the problem also happens with a single sleep(2.0).
        await asyncio.sleep(0.1)
    
    process.terminate() # This unexpectedly errors with ProcessLookupError.

    print(await process.wait())

asyncio.set_child_watcher(WATCHER_CLASS())
asyncio.run(main())
