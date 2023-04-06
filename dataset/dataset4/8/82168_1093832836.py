def crash():
    for i in [1, 2, 3]:
        try:
            return i
        finally:
            continue


crash()