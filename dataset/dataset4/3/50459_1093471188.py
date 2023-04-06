def process(iterable):
    try:
        x = next(iterable)
    except StopIteration:
        raise ValueError("can't process empty iterable")
    continue_processing()