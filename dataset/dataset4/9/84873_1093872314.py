# If we have an exception, run the function inside the except block
# after raising it so exc_info is correctly populated.
if exc_info[1]:
    try:
        raise exc_info[1]
    except:
        return func(*args, **kwargs)
else:
    return func(*args, **kwargs)