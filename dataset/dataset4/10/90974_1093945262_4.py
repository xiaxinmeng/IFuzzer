ret = asyncio.run(ContextOpener(open_test(), feeds.AsyncFileFeed))
print("Finish:", ret)