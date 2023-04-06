from multiprocessing import Pool


def f(x):
    return x * x


def s(x):
    print(f'Here: {x}')
    return type(x)


if __name__ == '__main__':
    with Pool(5) as p:
        result = p.map_async(f, [1, 2, 3], callback=s)
        q = result.get()
        print(q)