import sys

async def open_file():
    pass

async def main():
    open_file_coro = open_file()
    print("refcount:", sys.getrefcount(open_file_coro))