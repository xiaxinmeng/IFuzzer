
# wait until the future completes or the timeout
try:
    await waiter
except exceptions.CancelledError:
    if fut.done():
        # What to do here? Either choice might be wrong!
        sys.exit( "Does not compute!" )
