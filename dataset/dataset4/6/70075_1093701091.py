async def foo():
    return 123

print(await foo())   # will print 123
print(await foo())   # prints None
print(await foo())   # prints None