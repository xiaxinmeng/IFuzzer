last = next(it)
for x in it:
    process(last)
    last = x
special_handling(last)