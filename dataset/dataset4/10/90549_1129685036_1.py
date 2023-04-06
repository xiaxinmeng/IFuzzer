import multiprocessing as mp


def submain():
    pass


if __name__ == '__main__':
    global_resource = mp.Semaphore()
    p = mp.Process(target=submain)
    p.start()
    p.join()
