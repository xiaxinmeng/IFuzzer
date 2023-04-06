def test():
    start = time.time()
    end = datetime.datetime.now()
    start = datetime.datetime.fromtimestamp(start, None)
    assert end >= start