if __name__ == "__main__":
    async def open_test():
        await asyncio.sleep(1)
        return 1

    async def main():
        c = ContextOpener(open_test(), feeds.AsyncFileFeed)
        ret = await c
        print("Finish:", ret, ret._handle)