def compute_stuff(i):
    # in real life you could use a lib that uses threads
    # like cuda and that would crash with the default 'fork'
    # mode under POSIX
    return i ** 2


if __name__ == "__main__":
     freeze_support()
     ctx = get_context('spawn')
     ctx.Pool(4).map(compute_stuff, range(8))