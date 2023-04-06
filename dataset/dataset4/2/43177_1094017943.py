def d(dir):
    return [fn
            for fn in os.listdir(dir)
            if fn
            if fn]