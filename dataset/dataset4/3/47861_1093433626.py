def f():
    class Bug:
        def __del__(self):
            1/0

    import gc
    trash = [Bug()]
    trash.append(trash)
    try:
        gc.collect()
        gc.set_threshold(1, 1, 1)
        del trash
        len()
    except TypeError:
        raise

if __name__ == "__main__":
    f()