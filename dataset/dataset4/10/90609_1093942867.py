stop = 0
def trace(frame, event, arg):
    global stop
    if stop > 10:
        return None

    if np.core.numeric.dtype is not np.dtype:
        #print("Something happened here, `np.core.numeric.dtype IS np.dtype`")
        print(np.core.numeric.dtype)
        print(frame, event, arg)
        stop += 1
    else:
        print(frame, event, arg)

    return trace