import multiprocessing.dummy as mp


def test(n):
    raise


def main():
    pool = mp.Pool(2)

    result = pool.map(test, [1])
    print(list(result))


if __name__ == '__main__':
    main()
