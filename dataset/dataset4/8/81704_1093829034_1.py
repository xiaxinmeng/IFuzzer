def test():
    with zipfile.ZipFile(test_zip) as zf:
        for i in range(100000):
            zf.read(test_name)


if __name__ == "__main__":
    import timeit
    print(timeit.repeat("test()", setup="from __main__ import test", number=1, repeat=10))