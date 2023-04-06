# This is an example function that possibly raises `StopIteration`.
# In some cases, this function may raise `StopIteration` in the first iteration.
def raise_stop_iteration(param):
    if param == 10:
        raise StopIteration
    # Suppose this function will do some simple calculation
    return -param