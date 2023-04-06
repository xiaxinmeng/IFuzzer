async def test():
    print(await no_error())  # False
    print(await error())     # RuntimeWarning(...), False


if __name__ == '__main__':
    run(test())