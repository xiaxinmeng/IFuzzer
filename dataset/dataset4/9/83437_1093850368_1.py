def exception_handler(loop, context):
    exception = context.get("exception", None)
    print("exception_handler", exception)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(exception_handler)
    loop.run_until_complete(main())
    print("Job done")